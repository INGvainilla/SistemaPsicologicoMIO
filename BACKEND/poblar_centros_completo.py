import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sigepsi.settings')
django.setup()

from django_tenants.utils import schema_context
from apps.users.models import Usuario, Rol, Permiso
from apps.tenants.models import Centro, Dominio

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

CENTROS_CONFIG = [
    {
        'name': 'Sanamente - Clínica Psicológica',
        'schema_name': 'clinica_demo',
        'domains': ['sanamente.localhost', '192.168.0.8', 'localhost'],
        'admin': {
            'email': 'admin.sanamente@sigepsi.com',
            'first_name': 'Roberto',
            'last_name': 'Sanabria (Jefe)',
            'phone': '+591 70011223',
        },
        'psicologos': [
            {
                'email': 'psicologo1.sanamente@sigepsi.com',
                'first_name': 'Carmen',
                'last_name': 'Mendoza',
                'phone': '+591 71122334',
            },
            {
                'email': 'psicologo2.sanamente@sigepsi.com',
                'first_name': 'Alejandro',
                'last_name': 'Flores',
                'phone': '+591 72233445',
            }
        ],
        'pacientes': [
            {
                'email': 'paciente.sanamente@sigepsi.com',
                'first_name': 'María',
                'last_name': 'López',
                'phone': '+591 73344556',
            }
        ]
    },
    {
        'name': 'MenteSana - Centro de Atención Psicológica',
        'schema_name': 'mentesana',
        'domains': ['mentesana.localhost'],
        'admin': {
            'email': 'admin.mentesana@sigepsi.com',
            'first_name': 'Fernando',
            'last_name': 'Morales (Jefe)',
            'phone': '+591 74455667',
        },
        'psicologos': [
            {
                'email': 'psicologo1.mentesana@sigepsi.com',
                'first_name': 'Valeria',
                'last_name': 'Quispe',
                'phone': '+591 75566778',
            },
            {
                'email': 'psicologo2.mentesana@sigepsi.com',
                'first_name': 'Gabriel',
                'last_name': 'Torrez',
                'phone': '+591 76677889',
            }
        ],
        'pacientes': [
            {
                'email': 'paciente.mentesana@sigepsi.com',
                'first_name': 'Carlos',
                'last_name': 'Gutiérrez',
                'phone': '+591 77788990',
            }
        ]
    },
    {
        'name': 'Equilibrio - Instituto Psicoterapéutico',
        'schema_name': 'equilibrio',
        'domains': ['equilibrio.localhost'],
        'admin': {
            'email': 'admin.equilibrio@sigepsi.com',
            'first_name': 'Patricia',
            'last_name': 'Arze (Jefe)',
            'phone': '+591 78899001',
        },
        'psicologos': [
            {
                'email': 'psicologo1.equilibrio@sigepsi.com',
                'first_name': 'Diego',
                'last_name': 'Navarro',
                'phone': '+591 79900112',
            },
            {
                'email': 'psicologo2.equilibrio@sigepsi.com',
                'first_name': 'Sofía',
                'last_name': 'Rojas',
                'phone': '+591 70099887',
            }
        ],
        'pacientes': [
            {
                'email': 'paciente.equilibrio@sigepsi.com',
                'first_name': 'Lucía',
                'last_name': 'Vargas',
                'phone': '+591 71188776',
            }
        ]
    }
]

def setup_roles_for_schema(schema_name):
    with schema_context(schema_name):
        permisos_dict = {}
        for name, codename in permisos_base:
            p, _ = Permiso.objects.get_or_create(codename=codename, defaults={'name': name})
            permisos_dict[codename] = p

        rol_super, _ = Rol.objects.get_or_create(
            name='SuperAdmin',
            defaults={'description': 'Administrador global del sistema con acceso total.'}
        )
        rol_super.permisos.set(list(permisos_dict.values()))

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

        rol_paciente, _ = Rol.objects.get_or_create(
            name='Paciente',
            defaults={'description': 'Usuario paciente del centro.'}
        )
        rol_paciente.permisos.set([
            permisos_dict['ver_dashboard'],
            permisos_dict['gestionar_citas'],
        ])

def create_or_update_user(schema_name, email, first_name, last_name, phone, role_name, password='Sigepsi2026!'):
    with schema_context(schema_name):
        email_clean = email.strip().lower()
        user, _ = Usuario.objects.get_or_create(
            email=email_clean,
            defaults={
                'username': email_clean,
                'first_name': first_name,
                'last_name': last_name,
                'phone': phone,
                'is_active': True,
                'is_staff': role_name in ['SuperAdmin', 'AdminCentro'],
                'is_superuser': role_name == 'SuperAdmin',
            }
        )
        user.first_name = first_name
        user.last_name = last_name
        user.phone = phone
        user.is_active = True
        user.is_staff = role_name in ['SuperAdmin', 'AdminCentro']
        user.is_superuser = role_name == 'SuperAdmin'
        user.set_password(password)
        user.save()

        rol_obj = Rol.objects.filter(name=role_name).first()
        if rol_obj:
            user.roles.add(rol_obj)
        return user

def main():
    print("============================================================")
    print("  POBLANDO SUPABASE CON 3 CENTROS, JEFES Y PSICÓLOGOS")
    print("============================================================")

    # 1. Asegurar esquema public
    setup_roles_for_schema('public')

    # SuperAdmin en public
    super_admin = create_or_update_user(
        'public',
        'admin@sigepsi.com',
        'Super',
        'Admin SIGEPSI',
        '+591 70000000',
        'SuperAdmin',
        'Sigepsi2026!'
    )
    print(f"  [OK] SuperAdmin global: admin@sigepsi.com / Sigepsi2026!")

    all_users_to_sync = [
        ('admin@sigepsi.com', 'Super', 'Admin SIGEPSI', '+591 70000000', 'SuperAdmin', 'Sigepsi2026!')
    ]

    # 2. Crear los 3 Centros en Supabase
    for cfg in CENTROS_CONFIG:
        schema_name = cfg['schema_name']
        print(f"\n--- Configurando Centro: {cfg['name']} ({schema_name}) ---")
        
        # Crear o actualizar Centro
        centro, created = Centro.objects.get_or_create(
            schema_name=schema_name,
            defaults={'name': cfg['name'], 'is_active': True}
        )
        if not created and centro.name != cfg['name']:
            centro.name = cfg['name']
            centro.save()

        # Configurar Dominios
        for d in cfg['domains']:
            Dominio.objects.get_or_create(
                domain=d,
                defaults={'tenant': centro, 'is_primary': (d == cfg['domains'][0])}
            )

        # Configurar roles del esquema
        setup_roles_for_schema(schema_name)

        # Crear Jefe / Admin del Centro
        adm = cfg['admin']
        create_or_update_user(
            schema_name,
            adm['email'],
            adm['first_name'],
            adm['last_name'],
            adm['phone'],
            'AdminCentro',
            'Sigepsi2026!'
        )
        all_users_to_sync.append((adm['email'], adm['first_name'], adm['last_name'], adm['phone'], 'AdminCentro', 'Sigepsi2026!'))
        print(f"  [OK] Jefe/Admin Centro: {adm['email']} ({adm['first_name']} {adm['last_name']})")

        # Crear los 2 Psicólogos
        for p in cfg['psicologos']:
            create_or_update_user(
                schema_name,
                p['email'],
                p['first_name'],
                p['last_name'],
                p['phone'],
                'Psicólogo',
                'Sigepsi2026!'
            )
            all_users_to_sync.append((p['email'], p['first_name'], p['last_name'], p['phone'], 'Psicólogo', 'Sigepsi2026!'))
            print(f"  [OK] Psicólogo: {p['email']} ({p['first_name']} {p['last_name']})")

        # Crear Paciente demo
        for pac in cfg['pacientes']:
            create_or_update_user(
                schema_name,
                pac['email'],
                pac['first_name'],
                pac['last_name'],
                pac['phone'],
                'Paciente',
                'Sigepsi2026!'
            )
            all_users_to_sync.append((pac['email'], pac['first_name'], pac['last_name'], pac['phone'], 'Paciente', 'Sigepsi2026!'))
            print(f"  [OK] Paciente: {pac['email']} ({pac['first_name']} {pac['last_name']})")

    # 3. Sincronizar todos los usuarios en el esquema public y en cada esquema
    print("\n--- Sincronizando todos los usuarios en public y esquemas activos ---")
    schemas_to_sync = ['public'] + [c['schema_name'] for c in CENTROS_CONFIG]
    for s_name in schemas_to_sync:
        for u_data in all_users_to_sync:
            email, f_name, l_name, phone, r_name, pwd = u_data
            create_or_update_user(s_name, email, f_name, l_name, phone, r_name, pwd)

    print("\n============================================================")
    print("  ¡POBLACIÓN DE 3 CENTROS COMPLETADA EXITOSAMENTE!")
    print("============================================================")

if __name__ == '__main__':
    main()
