import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sigepsi.settings')
django.setup()

from django_tenants.utils import schema_context
from apps.users.models import Usuario, Rol
from apps.tenants.models import Centro

# Obtener rol en public
with schema_context('public'):
    rol_admin_pub, _ = Rol.objects.get_or_create(
        name='AdminCentro',
        defaults={'description': 'Administrador general y jefe del centro psicológico.'}
    )

admins_to_sync = []

for c in Centro.objects.exclude(schema_name='public'):
    with schema_context(c.schema_name):
        admins = Usuario.objects.filter(roles__name__iexact='AdminCentro')
        for admin in admins:
            admins_to_sync.append({
                'email': admin.email,
                'username': admin.username or admin.email,
                'first_name': admin.first_name or 'Admin',
                'last_name': admin.last_name or c.name,
                'password': admin.password,
                'centro': c.name
            })

with schema_context('public'):
    for a in admins_to_sync:
        pub_u, created = Usuario.objects.get_or_create(
            email=a['email'],
            defaults={
                'username': a['username'],
                'first_name': a['first_name'],
                'last_name': a['last_name'],
                'is_staff': True,
                'is_active': True,
            }
        )
        pub_u.password = a['password']
        pub_u.first_name = a['first_name']
        pub_u.last_name = a['last_name']
        pub_u.is_staff = True
        pub_u.is_active = True
        pub_u.save()
        pub_u.roles.add(rol_admin_pub)
        print(f"Sincronizado a public: {a['email']} (Centro: {a['centro']})")

print("Sincronización completa con éxito.")
