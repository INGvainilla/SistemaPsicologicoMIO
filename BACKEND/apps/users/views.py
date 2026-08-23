from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils import timezone
from datetime import timedelta
import uuid

from .models import Usuario, Rol, Permiso, TokenRecuperacion
from .serializers import (
    UsuarioSerializer, RolSerializer, PermisoSerializer,
    PasswordResetRequestSerializer, PasswordResetConfirmSerializer
)

class PermisoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Permiso.objects.all()
    serializer_class = PermisoSerializer
    permission_classes = [IsAuthenticated]

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    permission_classes = [IsAuthenticated]

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

class PasswordResetViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'], url_path='request')
    def request_reset(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = Usuario.objects.filter(email=email).first()
            if user:
                # Generate token
                token_obj = TokenRecuperacion.objects.create(
                    usuario=user,
                    token=str(uuid.uuid4()),
                    fecha_expiracion=timezone.now() + timedelta(minutes=30)
                )
                from django.core.mail import send_mail
                from django.conf import settings
                
                reset_url = f"http://localhost:4200/password-reset/confirm?token={token_obj.token}"
                
                send_mail(
                    subject='Restablecer Contraseña (SIGEPSI)',
                    message=f'Hola,\n\nHaz clic en el siguiente enlace para crear tu nueva contraseña:\n{reset_url}\n\nSi no fuiste tú, ignora este mensaje.',
                    from_email=settings.EMAIL_HOST_USER if getattr(settings, 'EMAIL_HOST_USER', None) else 'no-reply@sigepsi.com',
                    recipient_list=[user.email],
                    fail_silently=False,
                )
                
            return Response({"message": "Si el correo existe, se ha enviado un enlace de recuperación."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='confirm')
    def confirm_reset(self, request):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.validated_data['token']
            new_password = serializer.validated_data['new_password']
            
            token_obj = TokenRecuperacion.objects.filter(
                token=token, 
                usado=False, 
                fecha_expiracion__gt=timezone.now()
            ).first()
            
            if not token_obj:
                return Response({"error": "Token inválido o expirado."}, status=status.HTTP_400_BAD_REQUEST)
                
            user = token_obj.usuario
            user.set_password(new_password)
            user.save()
            
            token_obj.usado = True
            token_obj.save()
            
            return Response({"message": "Contraseña actualizada exitosamente."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
