from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class Permiso(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    codename = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Rol(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    permisos = models.ManyToManyField(Permiso, related_name='roles')

    def __str__(self):
        return self.name

class Usuario(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # email will be used to login instead of username
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    roles = models.ManyToManyField(Rol, related_name='usuarios')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email

class ConfiguracionCentro(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address = models.CharField(max_length=255, blank=True, null=True)
    contact_email = models.EmailField(max_length=255, blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    logo_url = models.CharField(max_length=255, blank=True, null=True)
    primary_color = models.CharField(max_length=7, default='#FFFFFF')
