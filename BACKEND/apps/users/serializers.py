from rest_framework import serializers
from .models import Usuario, Rol, Permiso
from django.contrib.auth.hashers import make_password

class PermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = ['id', 'name', 'codename']

class RolSerializer(serializers.ModelSerializer):
    permisos_details = PermisoSerializer(source='permisos', many=True, read_only=True)
    permisos = serializers.PrimaryKeyRelatedField(
        queryset=Permiso.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = Rol
        fields = ['id', 'name', 'description', 'permisos', 'permisos_details']

class UsuarioSerializer(serializers.ModelSerializer):
    roles_details = RolSerializer(source='roles', many=True, read_only=True)
    roles = serializers.PrimaryKeyRelatedField(
        queryset=Rol.objects.all(),
        many=True,
        required=False
    )
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = Usuario
        fields = [
            'id', 'email', 'first_name', 'last_name', 
            'phone', 'password', 'is_active', 'roles', 'roles_details'
        ]

    def create(self, validated_data):
        roles_data = validated_data.pop('roles', [])
        validated_data['password'] = make_password(validated_data.get('password'))
        
        # When creating a user in django-tenants, they are created in the current tenant's schema
        user = Usuario.objects.create(**validated_data)
        
        if roles_data:
            user.roles.set(roles_data)
        return user

    def update(self, instance, validated_data):
        roles_data = validated_data.pop('roles', None)
        
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data.get('password'))

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        if roles_data is not None:
            instance.roles.set(roles_data)
            
        return instance

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

class PasswordResetConfirmSerializer(serializers.Serializer):
    token = serializers.CharField()
    new_password = serializers.CharField(write_only=True, min_length=8)
