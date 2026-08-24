import re
from rest_framework import serializers
from django_tenants.utils import schema_context
from .models import Centro, Dominio
from apps.users.models import Usuario, Rol, Permiso

class DominioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dominio
        fields = ['id', 'domain', 'is_primary']

class CentroSerializer(serializers.ModelSerializer):
    domains = DominioSerializer(many=True, read_only=True)
    domain_url = serializers.CharField(write_only=True, required=False)
    admin_name = serializers.CharField(write_only=True, required=False, default='Administrador de Centro')
    admin_email = serializers.EmailField(write_only=True, required=False, default='')
    admin_password = serializers.CharField(write_only=True, required=False, default='Sigepsi2026!')
    total_usuarios = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Centro
        fields = [
            'id', 'name', 'schema_name', 'is_active', 'created_at', 
            'domains', 'domain_url', 'admin_name', 'admin_email', 'admin_password',
            'total_usuarios'
        ]
        read_only_fields = ['id', 'created_at', 'total_usuarios']

    def validate_schema_name(self, value):
        value = value.lower().strip()
        if value in ['public', 'schema', 'information_schema', 'pg_catalog']:
            raise serializers.ValidationError('Este nombre de esquema está reservado.')
        if not re.match(r'^[a-z0-9_]+$', value):
            raise serializers.ValidationError('El identificador de esquema solo puede contener letras minúsculas, números y guiones bajos.')
        query = Centro.objects.filter(schema_name=value)
        if self.instance:
            query = query.exclude(id=self.instance.id)
        if query.exists():
            raise serializers.ValidationError('Ya existe un centro registrado con este identificador de esquema.')
        return value

    def get_total_usuarios(self, obj):
        try:
            with schema_context(obj.schema_name):
                return Usuario.objects.count()
        except Exception:
            return 0

    def create(self, validated_data):
        domain_url = validated_data.pop('domain_url', None)
        admin_name = validated_data.pop('admin_name', 'Administrador de Centro')
        admin_email = validated_data.pop('admin_email', '').strip().lower()
        admin_password = validated_data.pop('admin_password', 'Sigepsi2026!')

        # 1. Crear el tenant (PostgreSQL schema se genera automáticamente)
        tenant = Centro.objects.create(**validated_data)
        
        # 2. Crear el dominio principal
        domain_name = domain_url.strip().lower() if domain_url else f"{tenant.schema_name}.localhost"
        Dominio.objects.create(
            domain=domain_name,
            tenant=tenant,
            is_primary=True
        )

        target_email = admin_email if admin_email else f"admin.{tenant.schema_name}@sigepsi.com"
        first_name = admin_name.strip() if admin_name else 'Admin'
        pwd = admin_password if admin_password else 'Sigepsi2026!'

        # 3. Guardar al Administrador en el esquema público de forma explícita
        try:
            with schema_context('public'):
                rol_admin_public, _ = Rol.objects.get_or_create(
                    name='AdminCentro',
                    defaults={'description': 'Administrador general y jefe del centro psicológico.'}
                )
                admin_public, _ = Usuario.objects.get_or_create(
                    email=target_email,
                    defaults={
                        'username': target_email,
                        'first_name': first_name,
                        'last_name': tenant.name,
                        'is_staff': True,
                        'is_active': True,
                    }
                )
                admin_public.set_password(pwd)
                admin_public.first_name = first_name
                admin_public.last_name = tenant.name
                admin_public.is_staff = True
                admin_public.is_active = True
                admin_public.save()
                admin_public.roles.set([rol_admin_public])
        except Exception as e:
            print(f"Error registrando admin en esquema public: {e}")

        # 4. Auto-poblar el nuevo esquema con permisos, roles y el usuario administrador
        try:
            with schema_context(tenant.schema_name):
                # 4.1. Permisos base
                permisos_dict = {}
                permisos_base = [
                    ('Gestionar Usuarios', 'gestionar_usuarios'),
                    ('Gestionar Roles', 'gestionar_roles'),
                    ('Ver Dashboard', 'ver_dashboard'),
                    ('Gestionar Pacientes', 'gestionar_pacientes'),
                    ('Gestionar Citas', 'gestionar_citas'),
                    ('Ver Historial Clínico', 'ver_historial_clinico'),
                    ('Editar Historial Clínico', 'editar_historial_clinico'),
                ]
                for name, codename in permisos_base:
                    p, _ = Permiso.objects.get_or_create(codename=codename, defaults={'name': name})
                    permisos_dict[codename] = p

                # 4.2. Rol SuperAdmin
                rol_super, _ = Rol.objects.get_or_create(
                    name='SuperAdmin',
                    defaults={'description': 'Administrador global del sistema con acceso total.'}
                )
                rol_super.permisos.set(list(permisos_dict.values()))

                # 4.3. Rol AdminCentro
                rol_admin, _ = Rol.objects.get_or_create(
                    name='AdminCentro',
                    defaults={'description': 'Administrador general y jefe del centro psicológico.'}
                )
                rol_admin.permisos.set([
                    permisos_dict['gestionar_usuarios'],
                    permisos_dict['gestionar_roles'],
                    permisos_dict['ver_dashboard'],
                    permisos_dict['gestionar_pacientes'],
                    permisos_dict['gestionar_citas'],
                    permisos_dict['ver_historial_clinico'],
                    permisos_dict['editar_historial_clinico'],
                ])

                # 4.4. Rol Psicólogo
                rol_psico, _ = Rol.objects.get_or_create(
                    name='Psicólogo',
                    defaults={'description': 'Profesional de salud mental y atención clínica.'}
                )
                rol_psico.permisos.set([
                    permisos_dict['ver_dashboard'],
                    permisos_dict['gestionar_pacientes'],
                    permisos_dict['gestionar_citas'],
                    permisos_dict['ver_historial_clinico'],
                    permisos_dict['editar_historial_clinico'],
                ])

                # 4.5. Rol Recepcionista
                rol_recep, _ = Rol.objects.get_or_create(
                    name='Recepcionista',
                    defaults={'description': 'Personal de recepción y gestión de agenda.'}
                )
                rol_recep.permisos.set([
                    permisos_dict['ver_dashboard'],
                    permisos_dict['gestionar_pacientes'],
                    permisos_dict['gestionar_citas'],
                ])

                # 4.6. Rol Paciente
                rol_paciente, _ = Rol.objects.get_or_create(
                    name='Paciente',
                    defaults={'description': 'Paciente registrado en la clínica.'}
                )
                rol_paciente.permisos.set([
                    permisos_dict['ver_dashboard'],
                    permisos_dict['gestionar_citas'],
                ])

                # 4.7. Crear el usuario Administrador del Centro en el esquema aislado
                admin_tenant, _ = Usuario.objects.get_or_create(
                    email=target_email,
                    defaults={
                        'username': target_email,
                        'first_name': first_name,
                        'last_name': tenant.name,
                        'is_staff': True,
                        'is_active': True,
                    }
                )
                admin_tenant.set_password(pwd)
                admin_tenant.first_name = first_name
                admin_tenant.last_name = tenant.name
                admin_tenant.is_staff = True
                admin_tenant.is_active = True
                admin_tenant.save()
                admin_tenant.roles.set([rol_admin])

                # 4.8. Crear también usuario SuperAdmin dentro del esquema para soporte
                admin_global, _ = Usuario.objects.get_or_create(
                    email='admin@sigepsi.com',
                    defaults={
                        'username': 'admin@sigepsi.com',
                        'first_name': 'Administrador',
                        'last_name': 'Global',
                        'is_staff': True,
                        'is_superuser': True,
                        'is_active': True,
                    }
                )
                admin_global.set_password('Sigepsi2026!')
                admin_global.is_superuser = True
                admin_global.is_staff = True
                admin_global.save()
                admin_global.roles.set([rol_super])

        except Exception as e:
            print(f"Error poblando esquema {tenant.schema_name}: {e}")

        return tenant
