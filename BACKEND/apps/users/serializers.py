import re
from rest_framework import serializers
from .models import Usuario, Rol, Permiso
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from .tokens import resolve_reset_code

PACIENTE_ROLE_NAME = 'Paciente'

def validate_secure_password(value):
    if not value:
        return value
    if len(value) < 8:
        raise serializers.ValidationError('La contraseña debe tener al menos 8 caracteres.')
    if not re.search(r'[A-Z]', value):
        raise serializers.ValidationError('La contraseña debe contener al menos una letra mayúscula.')
    if not re.search(r'[a-z]', value):
        raise serializers.ValidationError('La contraseña debe contener al menos una letra minúscula.')
    if not re.search(r'\d', value):
        raise serializers.ValidationError('La contraseña debe contener al menos un número.')
    if not re.search(r'[^a-zA-Z0-9]', value):
        raise serializers.ValidationError('La contraseña debe contener al menos un carácter especial (ej. !, @, #, $, etc.).')
    return value

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
    permiso_ids = serializers.ListField(
        child=serializers.CharField(),
        write_only=True,
        required=False
    )

    class Meta:
        model = Rol
        fields = ['id', 'name', 'description', 'permisos', 'permisos_details', 'permiso_ids']

    def create(self, validated_data):
        permisos_data = validated_data.pop('permisos', [])
        permiso_ids = validated_data.pop('permiso_ids', [])
        rol = Rol.objects.create(**validated_data)
        
        if permiso_ids:
            perms = Permiso.objects.filter(id__in=permiso_ids)
            rol.permisos.set(perms)
        elif permisos_data:
            rol.permisos.set(permisos_data)
        return rol

    def update(self, instance, validated_data):
        permisos_data = validated_data.pop('permisos', None)
        permiso_ids = validated_data.pop('permiso_ids', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        if permiso_ids is not None:
            perms = Permiso.objects.filter(id__in=permiso_ids)
            instance.permisos.set(perms)
        elif permisos_data is not None:
            instance.permisos.set(permisos_data)
        return instance

class UsuarioSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, allow_blank=True, default='')
    roles_details = RolSerializer(source='roles', many=True, read_only=True)
    roles = serializers.PrimaryKeyRelatedField(
        queryset=Rol.objects.all(),
        many=True,
        required=False
    )
    role_ids = serializers.ListField(
        child=serializers.CharField(),
        write_only=True,
        required=False
    )
    roles_names = serializers.SerializerMethodField(read_only=True)
    password = serializers.CharField(
        write_only=True, 
        required=False, 
        allow_blank=True,
        style={'input_type': 'password'}, 
        validators=[validate_secure_password]
    )

    class Meta:
        model = Usuario
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name', 
            'phone', 'password', 'is_active', 'is_staff', 'is_superuser',
            'roles', 'roles_details', 'role_ids', 'roles_names'
        ]
        read_only_fields = ['id', 'roles_names']

    def get_roles_names(self, obj):
        return [r.name for r in obj.roles.all()]

    def validate_email(self, value):
        value = value.strip().lower()
        query = Usuario.objects.filter(email__iexact=value)
        if self.instance:
            query = query.exclude(id=self.instance.id)
        if query.exists():
            raise serializers.ValidationError('Ya existe una cuenta con este correo electrónico.')
        return value

    def validate(self, attrs):
        email = attrs.get('email', '')
        if email:
            attrs['username'] = email.strip().lower()
        elif self.instance and self.instance.email:
            attrs['username'] = self.instance.email.strip().lower()

        # Al crear un nuevo usuario, la contraseña es obligatoria
        if not self.instance and not attrs.get('password'):
            raise serializers.ValidationError({'password': 'La contraseña es requerida al crear un usuario.'})
        return attrs

    def create(self, validated_data):
        roles_data = validated_data.pop('roles', [])
        role_ids = validated_data.pop('role_ids', [])
        raw_password = validated_data.pop('password', None)
        
        email = validated_data.get('email', '').strip().lower()
        validated_data['email'] = email
        validated_data['username'] = email

        if raw_password:
            validated_data['password'] = make_password(raw_password)
        
        user = Usuario.objects.create(**validated_data)
        
        if role_ids:
            roles_found = Rol.objects.filter(id__in=role_ids)
            user.roles.set(roles_found)
        elif roles_data:
            user.roles.set(roles_data)
        return user

    def update(self, instance, validated_data):
        roles_data = validated_data.pop('roles', None)
        role_ids = validated_data.pop('role_ids', None)
        raw_password = validated_data.pop('password', None)
        
        if 'email' in validated_data:
            email = validated_data['email'].strip().lower()
            validated_data['email'] = email
            validated_data['username'] = email

        if raw_password:
            validated_data['password'] = make_password(raw_password)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        if role_ids is not None:
            roles_found = Rol.objects.filter(id__in=role_ids)
            instance.roles.set(roles_found)
        elif roles_data is not None:
            instance.roles.set(roles_data)
            
        return instance

class UserProfileSerializer(serializers.ModelSerializer):
    roles = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    roles_details = RolSerializer(source='roles', many=True, read_only=True)
    permisos = serializers.SerializerMethodField(read_only=True)
    tenant = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Usuario
        fields = [
            'id', 'email', 'first_name', 'last_name', 'phone', 
            'is_active', 'is_staff', 'is_superuser',
            'roles', 'roles_details', 'permisos', 'tenant'
        ]
        read_only_fields = fields

    def get_permisos(self, obj):
        if obj.is_superuser:
            return list(Permiso.objects.values_list('codename', flat=True))
        # Aprovecha prefetch_related ya cargado, sin queries extra
        permisos_set = set()
        for rol in obj.roles.all():
            permisos_set.update(p.codename for p in rol.permisos.all())
        return list(permisos_set)

    def get_tenant(self, obj):
        request = self.context.get('request')
        tenant = getattr(request, 'tenant', None)
        if tenant and tenant.schema_name != 'public':
            return {
                'id': tenant.id,
                'name': tenant.name,
                'schema_name': tenant.schema_name,
            }
        return {'id': 1, 'name': 'SIGEPSI Admin Global', 'schema_name': 'public'}

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        validators=[validate_secure_password],
    )
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = Usuario
        fields = ['id', 'email', 'password', 'first_name', 'last_name', 'phone']

    def validate_email(self, value):
        value = value.strip().lower()
        if Usuario.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError('Ya existe una cuenta registrada con este correo electrónico.')
        return value

    def create(self, validated_data):
        email = validated_data['email'].strip().lower()
        user = Usuario.objects.create_user(
            username=email,
            email=email,
            password=validated_data['password'],
            first_name=validated_data.get('first_name', '').strip(),
            last_name=validated_data.get('last_name', '').strip(),
            phone=validated_data.get('phone', '').strip(),
            is_active=True,
        )
        # Asignar rol Paciente por defecto
        paciente_role, _ = Rol.objects.get_or_create(
            name=PACIENTE_ROLE_NAME,
            defaults={'description': 'Paciente registrado en la clínica.'}
        )
        user.roles.add(paciente_role)
        return user

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

class PasswordResetConfirmSerializer(serializers.Serializer):
    token = serializers.CharField(required=False, allow_blank=True)
    code = serializers.CharField(required=False, allow_blank=True)
    new_password = serializers.CharField(
        write_only=True, 
        validators=[validate_secure_password]
    )

    def validate(self, attrs):
        if not attrs.get('token') and not attrs.get('code'):
            raise serializers.ValidationError("Debe proporcionar un 'token' o un 'code'.")
        return attrs

class MobilePasswordResetConfirmSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)
    new_password = serializers.CharField(
        write_only=True,
        validators=[validate_secure_password],
    )

class PasswordResetVerifySerializer(serializers.Serializer):
    code = serializers.CharField(required=True)

    def validate_code(self, value):
        user = resolve_reset_code(value)
        if not user:
            raise serializers.ValidationError('Código inválido o expirado.')
        return value
