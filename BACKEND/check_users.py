import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sigepsi.settings')
django.setup()

from django_tenants.utils import schema_context
from apps.users.models import Usuario, Rol, Permiso
from apps.tenants.models import Centro, Dominio

print('=================== CENTROS & DOMINIOS ===================')
for c in Centro.objects.all():
    doms = [d.domain for d in c.domains.all()]
    print(f"Centro ID: {c.id}, Name: {c.name}, Schema: {c.schema_name}, Active: {c.is_active}, Domains: {doms}")

print('\n=================== PUBLIC USERS ===================')
for u in Usuario.objects.all():
    print(f"Email: {u.email}, Active: {u.is_active}, Superuser: {u.is_superuser}, Roles: {[r.name for r in u.roles.all()]}")
    print(f"  Password match 'admin123': {u.check_password('admin123')}")
    print(f"  Password match 'Sigepsi2026!': {u.check_password('Sigepsi2026!')}")
    print(f"  Password match 'password123': {u.check_password('password123')}")

for c in Centro.objects.exclude(schema_name='public'):
    print(f"\n=================== SCHEMA: {c.schema_name} ===================")
    with schema_context(c.schema_name):
        for u in Usuario.objects.all():
            print(f"Email: {u.email}, Active: {u.is_active}, Superuser: {u.is_superuser}, Roles: {[r.name for r in u.roles.all()]}")
            print(f"  Password match 'admin123': {u.check_password('admin123')}")
            print(f"  Password match 'Sigepsi2026!': {u.check_password('Sigepsi2026!')}")
            print(f"  Password match 'password123': {u.check_password('password123')}")
