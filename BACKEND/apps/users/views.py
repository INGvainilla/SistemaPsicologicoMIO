from rest_framework import viewsets, status, generics, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
from datetime import timedelta
import uuid
from urllib.parse import urlparse
from django.conf import settings
from django.core.mail import send_mail
from django_tenants.utils import schema_context
from django.core.cache import cache
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

from .models import Usuario, Rol, Permiso, TokenRecuperacion
from .serializers import (
    UsuarioSerializer, RolSerializer, PermisoSerializer,
    PasswordResetRequestSerializer, PasswordResetConfirmSerializer,
    MobilePasswordResetConfirmSerializer, PasswordResetVerifySerializer,
    RegisterSerializer, UserProfileSerializer
)
from .tokens import make_reset_code, resolve_reset_code
from .permissions import CanManageUsers, CanManageRoles, IsSuperAdminUser
from apps.tenants.models import Centro

# --- ViewSets for Web & Management ---

class PermisoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Permiso.objects.all().order_by('name')
    serializer_class = PermisoSerializer
    permission_classes = [IsAuthenticated]

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all().prefetch_related('permisos').order_by('name')
    serializer_class = RolSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), CanManageRoles()]
        return [IsAuthenticated()]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # Proteger roles base del sistema
        system_roles = ['SuperAdmin', 'AdminCentro', 'Psicologo', 'Psicólogo', 'Paciente', 'Recepcionista']
        if instance.name in system_roles:
            return Response(
                {"error": f"El rol '{instance.name}' es fundamental para el sistema y no puede ser eliminado."},
                status=status.HTTP_400_BAD_REQUEST
            )
        # Verificar si hay usuarios asociados
        if instance.usuarios.exists():
            return Response(
                {"error": f"No se puede eliminar el rol '{instance.name}' porque tiene usuarios asignados. Reasigna los usuarios primero."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().destroy(request, *args, **kwargs)


def _fetch_users_from_schema(schema_name):
    """Obtiene usuarios de un esquema específico (para ejecutar en hilo)."""
    import django
    django.db.connections.close_all()
    results = []
    try:
        with schema_context(schema_name):
            for u in Usuario.objects.all().prefetch_related('roles', 'roles__permisos').order_by('-date_joined'):
                results.append({
                    'user': u,
                    'email': u.email.lower(),
                    'schema': schema_name,
                })
    except Exception as e:
        print(f"Error consultando esquema {schema_name}: {e}")
    return results


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all().prefetch_related('roles', 'roles__permisos').order_by('-date_joined')
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated, CanManageUsers]

    def list(self, request, *args, **kwargs):
        user = request.user
        is_super = user.is_superuser or user.roles.filter(name__iexact='SuperAdmin').exists()

        if is_super:
            all_users = []
            seen_emails = set()

            # 1. Esquema actual (query rápida)
            current_schema = getattr(request, 'tenant', None).schema_name if getattr(request, 'tenant', None) else 'public'
            for u in Usuario.objects.all().prefetch_related('roles', 'roles__permisos').order_by('-date_joined'):
                email_lower = u.email.lower()
                if email_lower not in seen_emails:
                    all_users.append(u)
                    seen_emails.add(email_lower)

            # 2. Recopilar esquemas pendientes
            other_schemas = []
            if current_schema != 'public':
                other_schemas.append('public')
            for c in Centro.objects.exclude(schema_name__in=['public', current_schema]):
                other_schemas.append(c.schema_name)

            # 3. Consultar esquemas en paralelo con threads
            if other_schemas:
                with ThreadPoolExecutor(max_workers=min(len(other_schemas), 4)) as executor:
                    futures = {executor.submit(_fetch_users_from_schema, s): s for s in other_schemas}
                    for future in as_completed(futures):
                        try:
                            for item in future.result():
                                if item['email'] not in seen_emails:
                                    all_users.append(item['user'])
                                    seen_emails.add(item['email'])
                        except Exception:
                            pass

            role_filter = request.query_params.get('role', None)
            search_query = request.query_params.get('search', None)

            if role_filter and role_filter != 'Todos':
                all_users = [u for u in all_users if any(r.name.lower() == role_filter.lower() for r in u.roles.all())]

            if search_query:
                sq = search_query.lower()
                all_users = [
                    u for u in all_users
                    if sq in u.email.lower()
                    or sq in (u.first_name or '').lower()
                    or sq in (u.last_name or '').lower()
                ]

            serializer = self.get_serializer(all_users, many=True)
            return Response(serializer.data)

        # Para administradores de centro o psicólogos, devolver usuarios del centro actual
        queryset = self.get_queryset()
        role_filter = request.query_params.get('role', None)
        if role_filter and role_filter != 'Todos':
            queryset = queryset.filter(roles__name__iexact=role_filter)
        search_query = request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(
                email__icontains=search_query
            ) | queryset.filter(
                first_name__icontains=search_query
            ) | queryset.filter(
                last_name__icontains=search_query
            )
        serializer = self.get_serializer(queryset.distinct(), many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        user = serializer.save()
        self._sync_user_across_schemas(user)

    def perform_update(self, serializer):
        user = serializer.save()
        self._sync_user_across_schemas(user)

    def perform_destroy(self, instance):
        email = instance.email.lower()
        super().perform_destroy(instance)
        # Eliminar también en otros esquemas si corresponde
        for c in Centro.objects.all():
            try:
                with schema_context(c.schema_name):
                    Usuario.objects.filter(email__iexact=email).delete()
            except Exception:
                pass

    def _sync_user_across_schemas(self, user):
        role_names = [r.name for r in user.roles.all()]
        current_schema = getattr(self.request, 'tenant', None).schema_name if getattr(self.request, 'tenant', None) else 'public'

        # Sincronizar a public
        if current_schema != 'public':
            try:
                with schema_context('public'):
                    pub_u, _ = Usuario.objects.get_or_create(
                        email=user.email.lower(),
                        defaults={
                            'username': user.email.lower(),
                            'first_name': user.first_name,
                            'last_name': user.last_name,
                            'phone': user.phone,
                            'is_staff': user.is_staff or 'SuperAdmin' in role_names or 'AdminCentro' in role_names,
                            'is_superuser': user.is_superuser or 'SuperAdmin' in role_names,
                            'is_active': user.is_active,
                        }
                    )
                    pub_u.first_name = user.first_name
                    pub_u.last_name = user.last_name
                    pub_u.phone = user.phone
                    pub_u.password = user.password
                    pub_u.is_active = user.is_active
                    pub_u.save()
                    for r_name in role_names:
                        r_obj, _ = Rol.objects.get_or_create(name=r_name)
                        pub_u.roles.add(r_obj)
            except Exception as e:
                print(f"Error sincronizando a public: {e}")

        # Sincronizar a todos los centros
        for c in Centro.objects.exclude(schema_name='public'):
            if c.schema_name != current_schema:
                try:
                    with schema_context(c.schema_name):
                        t_u, _ = Usuario.objects.get_or_create(
                            email=user.email.lower(),
                            defaults={
                                'username': user.email.lower(),
                                'first_name': user.first_name,
                                'last_name': user.last_name,
                                'phone': user.phone,
                                'is_staff': user.is_staff,
                                'is_active': user.is_active,
                            }
                        )
                        t_u.first_name = user.first_name
                        t_u.last_name = user.last_name
                        t_u.phone = user.phone
                        t_u.password = user.password
                        t_u.is_active = user.is_active
                        t_u.save()
                        for r_name in role_names:
                            r_obj, _ = Rol.objects.get_or_create(name=r_name)
                            t_u.roles.add(r_obj)
                except Exception as e:
                    print(f"Error sincronizando a tenant {c.schema_name}: {e}")

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.id == request.user.id:
            return Response(
                {"error": "No puedes eliminar tu propia cuenta de usuario activa."},
                status=status.HTTP_400_BAD_REQUEST
            )
        if instance.is_superuser and not request.user.is_superuser:
            return Response(
                {"error": "No tienes permisos para eliminar a un SuperAdministrador."},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().destroy(request, *args, **kwargs)

class PasswordResetViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]
    GENERIC_MESSAGE = 'Si el correo está registrado, recibirás un mensaje con las instrucciones para restablecer tu contraseña.'

    @action(detail=False, methods=['post'], url_path='request')
    def request_reset(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email'].strip().lower()
            
            # Buscar el usuario en el esquema actual
            user = Usuario.objects.filter(email__iexact=email).first()
            target_schema = getattr(request, 'tenant', None).schema_name if getattr(request, 'tenant', None) else 'public'

            # Si no se encuentra en el esquema actual, buscar en public o en otros esquemas
            if not user and target_schema != 'public':
                with schema_context('public'):
                    user = Usuario.objects.filter(email__iexact=email).first()
                    if user:
                        target_schema = 'public'

            if not user:
                for c in Centro.objects.all():
                    with schema_context(c.schema_name):
                        found_u = Usuario.objects.filter(email__iexact=email).first()
                        if found_u:
                            user = found_u
                            target_schema = c.schema_name
                            break

            if user:
                with schema_context(target_schema):
                    # 1. Crear Token UUID para enlace Web
                    token_obj = TokenRecuperacion.objects.create(
                        usuario=user,
                        token=str(uuid.uuid4()),
                        fecha_expiracion=timezone.now() + timedelta(minutes=15)
                    )
                    
                    # 2. Crear Código corto para App Móvil
                    code = make_reset_code(user)
                    
                    # 3. Detectar origen para URL web
                    origin = request.headers.get('Origin') or request.headers.get('Referer')
                    if origin:
                        parsed = urlparse(origin)
                        base_origin = f"{parsed.scheme}://{parsed.netloc}"
                    else:
                        base_origin = "http://localhost:4200"
                    
                    reset_url = f"{base_origin}/password-reset/confirm?token={token_obj.token}"
                    
                    try:
                        from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', None) or getattr(settings, 'EMAIL_HOST_USER', 'no-reply@sigepsi.com')
                        send_mail(
                            subject='SIGEPSI - Restablecer Contraseña',
                            message=(
                                f'Hola {user.first_name or user.email},\n\n'
                                f'Recibimos una solicitud para restablecer tu contraseña en SIGEPSI.\n\n'
                                f'1. Desde la plataforma Web, haz clic en este enlace para crear tu nueva contraseña:\n{reset_url}\n\n'
                                f'2. Desde la App Móvil, puedes ingresar este código de verificación: {code}\n\n'
                                f'Este enlace y código expiran en 15 minutos.\n\n'
                                f'Si no solicitaste este cambio, puedes ignorar este mensaje.'
                            ),
                            from_email=from_email,
                            recipient_list=[user.email],
                            fail_silently=False,
                        )
                        print(f"[EMAIL OK] Enlace de recuperación enviado exitosamente a {user.email}")
                    except Exception as mail_err:
                        print(f"[EMAIL ERROR] Error enviando correo: {mail_err}")
                
            return Response({"detail": self.GENERIC_MESSAGE, "message": self.GENERIC_MESSAGE}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='confirm')
    def confirm_reset(self, request):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.validated_data.get('token')
            code = serializer.validated_data.get('code')
            new_password = serializer.validated_data['new_password']
            
            user = None
            token_obj = None
            found_schema = None
            
            # 1. Buscar en el esquema actual
            if token:
                token_obj = TokenRecuperacion.objects.filter(
                    token=token, 
                    usado=False, 
                    fecha_expiracion__gt=timezone.now()
                ).first()
                if token_obj:
                    user = token_obj.usuario
            
            if not user and code:
                user = resolve_reset_code(code)

            # 2. Si no se encontró en el esquema actual, buscar en todos los esquemas
            if not user and token:
                for c in Centro.objects.all():
                    with schema_context(c.schema_name):
                        t_obj = TokenRecuperacion.objects.filter(
                            token=token, 
                            usado=False, 
                            fecha_expiracion__gt=timezone.now()
                        ).first()
                        if t_obj:
                            user = t_obj.usuario
                            token_obj = t_obj
                            found_schema = c.schema_name
                            break
            
            if not user:
                err_msg = "El enlace o código de recuperación no es válido o ya expiró. Solicita uno nuevo."
                err_resp = {"error": err_msg, "detail": err_msg}
                if code:
                    err_resp["code"] = [err_msg]
                if token:
                    err_resp["token"] = [err_msg]
                return Response(err_resp, status=status.HTTP_400_BAD_REQUEST)
                
            # Guardar nueva contraseña en todos los esquemas donde exista el usuario
            for c in Centro.objects.all():
                try:
                    with schema_context(c.schema_name):
                        found_u = Usuario.objects.filter(email__iexact=user.email).first()
                        if found_u:
                            found_u.set_password(new_password)
                            found_u.save()
                        t_obj = TokenRecuperacion.objects.filter(token=token).first() if token else None
                        if t_obj:
                            t_obj.usado = True
                            t_obj.save()
                except Exception:
                    pass
                
            return Response(
                {"detail": "Contraseña actualizada exitosamente.", "message": "Contraseña actualizada exitosamente."},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- APIViews for Mobile & Profile ---

class RegisterView(APIView):
    """Registro de pacientes desde la aplicación móvil o web (HU-02)."""
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                'user': UserProfileSerializer(user, context={'request': request}).data,
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            },
            status=status.HTTP_201_CREATED,
        )

class PasswordResetRequestView(APIView):
    """HU-10a / CU27 / RF-31: solicitud de recuperación de contraseña."""
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        view = PasswordResetViewSet()
        return view.request_reset(request)

class PasswordResetVerifyView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = PasswordResetVerifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'detail': 'Código válido.'}, status=status.HTTP_200_OK)

class PasswordResetConfirmView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        view = PasswordResetViewSet()
        return view.confirm_reset(request)

class MeView(generics.RetrieveAPIView):
    """Perfil del usuario autenticado con roles, permisos y centro asignado."""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
