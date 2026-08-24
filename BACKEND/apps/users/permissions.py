from rest_framework import permissions

class IsSuperAdminUser(permissions.BasePermission):
    """
    Permite acceso únicamente a SuperAdministradores globales del sistema.
    """
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        user_roles = [r.lower() for r in request.user.roles.values_list('name', flat=True)]
        return 'superadmin' in user_roles

class CanManageTenants(permissions.BasePermission):
    """
    Permiso para gestionar Centros Psicológicos (Tenants).
    """
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        user_roles = [r.lower() for r in request.user.roles.values_list('name', flat=True)]
        if 'superadmin' in user_roles:
            return True
        return request.user.roles.filter(permisos__codename='gestionar_centros').exists()

class CanManageUsers(permissions.BasePermission):
    """
    Permiso para gestionar Usuarios en el centro actual o globalmente.
    """
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.user.is_superuser or request.user.is_staff:
            return True
        user_roles = [r.lower() for r in request.user.roles.values_list('name', flat=True)]
        if 'superadmin' in user_roles or 'admincentro' in user_roles or 'admin' in user_roles:
            return True
        return request.user.roles.filter(permisos__codename='gestionar_usuarios').exists()

class CanManageRoles(permissions.BasePermission):
    """
    Permiso para gestionar Roles y Permisos en el centro actual o globalmente.
    """
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.user.is_superuser or request.user.is_staff:
            return True
        user_roles = [r.lower() for r in request.user.roles.values_list('name', flat=True)]
        if 'superadmin' in user_roles or 'admincentro' in user_roles or 'admin' in user_roles:
            return True
        return request.user.roles.filter(permisos__codename='gestionar_roles').exists()
