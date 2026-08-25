#!/usr/bin/env python
"""
Registra dominios de producción (Railway, Vercel, etc.) en la tabla de
Dominios de django-tenants apuntando al tenant 'public'.

Uso:
    python add_production_domain.py <dominio>

Ejemplo:
    python add_production_domain.py sigepsi-production.up.railway.app
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sigepsi.settings')
django.setup()

from apps.tenants.models import Centro, Dominio


def add_domain(domain_name):
    domain_name = domain_name.strip().lower()
    if not domain_name:
        print("Error: Debe proporcionar un nombre de dominio.")
        sys.exit(1)

    # Obtener el tenant público
    try:
        public_tenant = Centro.objects.get(schema_name='public')
    except Centro.DoesNotExist:
        print("Error: No se encontró el tenant público. Ejecuta las migraciones primero.")
        sys.exit(1)

    # Crear o verificar dominio
    dominio, created = Dominio.objects.get_or_create(
        domain=domain_name,
        defaults={'tenant': public_tenant, 'is_primary': False}
    )

    if created:
        print(f"[OK] Dominio '{domain_name}' registrado exitosamente (tenant: public)")
    else:
        print(f"[INFO] El dominio '{domain_name}' ya estaba registrado (tenant: {dominio.tenant.schema_name})")

    # Listar todos los dominios actuales
    print("\nDominios registrados:")
    for d in Dominio.objects.all().select_related('tenant'):
        primary = " (PRIMARY)" if d.is_primary else ""
        print(f"  - {d.domain} -> {d.tenant.schema_name}{primary}")


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        add_domain(sys.argv[1])
    else:
        # Detectar variables de Railway o Vercel
        domains_to_add = []
        for env_var in ['RAILWAY_PUBLIC_DOMAIN', 'RAILWAY_STATIC_URL', 'CUSTOM_DOMAIN']:
            val = os.getenv(env_var, '').strip()
            # Limpiar https:// o http:// si vienen incluidos
            val = val.replace('https://', '').replace('http://', '').split('/')[0]
            if val and val not in domains_to_add:
                domains_to_add.append(val)

        if domains_to_add:
            for d in domains_to_add:
                add_domain(d)
        else:
            print("[INFO] No se detectó dominio en variables de entorno (RAILWAY_PUBLIC_DOMAIN). Continuando sin registrar dominio.")
            sys.exit(0)

