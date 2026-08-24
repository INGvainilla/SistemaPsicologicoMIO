import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sigepsi.settings')
django.setup()

from django.core.mail import send_mail
from django.conf import settings

print(f"Backend: {settings.EMAIL_BACKEND}")
print(f"Host: {settings.EMAIL_HOST}:{settings.EMAIL_PORT}")
print(f"User: {settings.EMAIL_HOST_USER}")
print(f"From: {settings.DEFAULT_FROM_EMAIL}")

try:
    send_mail(
        subject='[SIGEPSI] Prueba de Envío de Correo Real',
        message='¡Hola! Este es un correo de prueba enviado desde SIGEPSI para verificar la conexión SMTP con Gmail.',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=['mrgrueso2005@gmail.com'],
        fail_silently=False,
    )
    print("\n>>> CORREO ENVIADO EXITOSAMENTE POR GMAIL SMTP <<<")
except Exception as e:
    print(f"\n>>> ERROR ENVIANDO CORREO: {e} <<<")
