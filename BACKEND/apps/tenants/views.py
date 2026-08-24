from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Centro, Dominio
from .serializers import CentroSerializer, DominioSerializer
from apps.users.permissions import CanManageTenants

class CentroViewSet(viewsets.ModelViewSet):
    queryset = Centro.objects.all().order_by('-created_at')
    serializer_class = CentroSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Si el usuario es SuperAdmin (is_superuser o rol SuperAdmin), ve todos los centros
        if user.is_superuser or user.roles.filter(name__iexact='SuperAdmin').exists():
            return Centro.objects.all().order_by('-created_at')
        
        # En caso contrario, únicamente ve su propio tenant actual
        tenant = getattr(self.request, 'tenant', None)
        if tenant:
            return Centro.objects.filter(id=tenant.id)
        return Centro.objects.none()

    def get_permissions(self):
        # Crear, editar o eliminar centros requiere permisos de gestión de tenants (SuperAdmin)
        if self.action in ['create', 'update', 'partial_update', 'destroy', 'toggle_active']:
            return [IsAuthenticated(), CanManageTenants()]
        return [IsAuthenticated()]

    @action(detail=True, methods=['post'], url_path='toggle-active')
    def toggle_active(self, request, pk=None):
        centro = self.get_object()
        if centro.schema_name == 'public':
            return Response(
                {"error": "No se puede desactivar el tenant público principal."}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        centro.is_active = not centro.is_active
        centro.save(update_fields=['is_active'])
        return Response(
            {"message": f"Centro '{centro.name}' ahora está {'activo' if centro.is_active else 'inactivo'}.", "is_active": centro.is_active},
            status=status.HTTP_200_OK
        )
