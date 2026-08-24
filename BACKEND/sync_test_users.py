import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sigepsi.settings')
django.setup()

from django_tenants.utils import schema_context
from apps.users.models import Usuario, Rol, Permiso
from apps.tenants.models import Centro, Dominio

# 1. Permisos base
permisos_base = [
    ('Gestionar Usuarios', 'gestionar_usuarios'),
    ('Gestionar Roles', 'gestionar_roles'),
    ('Gestionar Centros', 'gestionar_centros'),
    ('Ver Dashboard', 'ver_dashboard'),
    ('Gestionar Pacientes', 'gestionar_pacientes'),
    ('Gestionar Citas', 'gestionar_citas'),
    ('Ver Historial Clínico', 'ver_historial_clinico'),
    ('Editar Historial Clínico', 'editar_historial_clinico'),
]

def setup_schema_data(schema_name):
    with schema_context(schema_name):
        print(f"\n--- Sincronizando esquema: {schema_name} ---")
        permisos_dict = {}
        for name, codename in permisos_base:
            p, _ = Permiso.objects.get_or_create(codename=codename, defaults={'name': name})
            permisos_dict[codename] = p

        # Rol SuperAdmin
        rol_super, _ = Rol.objects.get_or_create(
            name='SuperAdmin',
            defaults={'description': 'Administrador global del sistema con acceso total.'}
        )
        rol_super.permisos.set(list(permisos_dict.values()))

        # Rol AdminCentro
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

        # Rol Psicólogo
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

        # Rol Recepcionista
        rol_recep, _ = Rol.objects.get_or_create(
            name='Recepcionista',
            defaults={'description': 'Personal de recepción y gestión de agenda.'}
        )
        rol_recep.permisos.set([
            permisos_dict['ver_dashboard'],
            permisos_dict['gestionar_pacientes'],
            permisos_dict['gestionar_citas'],
        ])

        # Rol Paciente
        rol_paciente, _ = Rol.objects.get_or_create(
            name='Paciente',
            defaults={'description': 'Paciente registrado en la clínica.'}
        )
        rol_paciente.permisos.set([
            permisos_dict['ver_dashboard'],
            permisos_dict['gestionar_citas'],
        ])

        # SuperAdmin: admin@sigepsi.com / Sigepsi2026!
        u_admin, _ = Usuario.objects.get_or_create(
            email='admin@sigepsi.com',
            defaults={
                'username': 'admin',
                'first_name': 'Administrador',
                'last_name': 'Global',
                'is_staff': True,
                'is_superuser': True,
                'is_active': True,
            }
        )
        u_admin.set_password('Sigepsi2026!')
        u_admin.is_superuser = True
        u_admin.is_staff = True
        u_admin.is_active = True
        u_admin.save()
        u_admin.roles.set([rol_super])
        print(f"  [OK] SuperAdmin: admin@sigepsi.com / Sigepsi2026!")

        if schema_name != 'public':
            # Admin de Centro: admin.sanamente@sigepsi.com / Sigepsi2026!
            u_jefe, _ = Usuario.objects.get_or_create(
                email='admin.sanamente@sigepsi.com',
                defaults={
                    'username': 'admin.sanamente',
                    'first_name': 'Dra. María',
                    'last_name': 'Jefa de Centro',
                    'is_staff': True,
                    'is_superuser': False,
                    'is_active': True,
                }
            )
            u_jefe.set_password('Sigepsi2026!')
            u_jefe.is_active = True
            u_jefe.save()
            u_jefe.roles.set([rol_admin])
            print(f"  [OK] AdminCentro: admin.sanamente@sigepsi.com / Sigepsi2026!")

            # Psicólogo: psicologo@sanamente.com / password123 (o Sigepsi2026!)
            u_psico, _ = Usuario.objects.get_or_create(
                email='psicologo@sanamente.com',
                defaults={
                    'username': 'psicologo',
                    'first_name': 'Dr. Carlos',
                    'last_name': 'López',
                    'is_staff': False,
                    'is_superuser': False,
                    'is_active': True,
                }
            )
            u_psico.set_password('password123')
            u_psico.is_active = True
            u_psico.save()
            u_psico.roles.set([rol_psico])
            print(f"  [OK] Psicólogo: psicologo@sanamente.com / password123")

            # Paciente: paciente@sanamente.com / password123 (o Sigepsi2026!)
            u_pac, _ = Usuario.objects.get_or_create(
                email='paciente@sanamente.com',
                defaults={
                    'username': 'paciente',
                    'first_name': 'Ana',
                    'last_name': 'Martínez',
                    'is_staff': False,
                    'is_superuser': False,
                    'is_active': True,
                }
            )
            u_pac.set_password('password123')
            u_pac.is_active = True
            u_pac.save()
            u_pac.roles.set([rol_paciente])
            print(f"  [OK] Paciente: paciente@sanamente.com / password123")

# Sincronizar public
setup_schema_data('public')

# Sincronizar todos los tenants
for c in Centro.objects.exclude(schema_name='public'):
    setup_schema_data(c.schema_name)

print("\n============================================================")
print("  USUARIOS Y CONTRASEÑAS SINCRONIZADOS EXITOSAMENTE")
print("============================================================")
