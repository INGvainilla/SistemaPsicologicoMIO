import os
from pathlib import Path
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables
load_dotenv(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-default')
DEBUG = os.getenv('DEBUG', 'True') == 'True'

# Hosts permitidos
ALLOWED_HOSTS = ['*', 'localhost', '127.0.0.1', '.up.railway.app', '.vercel.app']
env_hosts = os.getenv('ALLOWED_HOSTS', '')
if env_hosts and env_hosts != '*':
    ALLOWED_HOSTS.extend(env_hosts.split(','))

# CSRF: confiar en dominios de Railway y Vercel en producción
CSRF_TRUSTED_ORIGINS = [
    'https://sistemapsicologicomio-production.up.railway.app',
    'https://*.up.railway.app',
    'https://*.vercel.app',
]
RAILWAY_URL = os.getenv('RAILWAY_STATIC_URL', os.getenv('RAILWAY_PUBLIC_DOMAIN', ''))
if RAILWAY_URL:
    CSRF_TRUSTED_ORIGINS.append(f'https://{RAILWAY_URL}')
VERCEL_URL = os.getenv('VERCEL_URL', '')
if VERCEL_URL:
    CSRF_TRUSTED_ORIGINS.append(f'https://{VERCEL_URL}')

# Email settings
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

if EMAIL_HOST_USER and EMAIL_HOST_PASSWORD:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
else:
    # Prints to console if no email is configured
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Application definition
SHARED_APPS = (
    'django_tenants',  # mandatory
    'apps.tenants', # you must list the app where your tenant model resides in

    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # third-party
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    
    # local
    'apps.users',
)

TENANT_APPS = (
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third-party
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    
    # local
    'apps.users',
)

INSTALLED_APPS = list(SHARED_APPS) + [app for app in TENANT_APPS if app not in SHARED_APPS]

TENANT_MODEL = "tenants.Centro"
TENANT_DOMAIN_MODEL = "tenants.Dominio"

MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Servir archivos estáticos en producción
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sigepsi.urls'
PUBLIC_SCHEMA_URLCONF = 'sigepsi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sigepsi.wsgi.application'

# Configuración de Base de Datos PostgreSQL / Supabase
db_sslmode = os.getenv('DB_SSLMODE', '').strip()
db_options = {}
if db_sslmode:
    db_options['sslmode'] = db_sslmode
elif os.getenv('DB_HOST', '') not in ['localhost', '127.0.0.1', '']:
    # Supabase y proveedores en la nube requieren SSL obligatorio
    db_options['sslmode'] = 'require'

DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': os.getenv('DB_NAME', 'postgres'),
        'USER': os.getenv('DB_USER', 'postgres'),
        'PASSWORD': os.getenv('DB_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
        'CONN_MAX_AGE': int(os.getenv('DB_CONN_MAX_AGE', '600')),
        'CONN_HEALTH_CHECKS': True,
        'OPTIONS': db_options,
    }
}
DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)

AUTH_USER_MODEL = 'users.Usuario'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'America/La_Paz'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS — en producción restringir a dominios conocidos
if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True
else:
    CORS_ALLOW_ALL_ORIGINS = False
    CORS_ALLOWED_ORIGINS = []
    if RAILWAY_URL:
        CORS_ALLOWED_ORIGINS.append(f'https://{RAILWAY_URL}')
    if VERCEL_URL:
        CORS_ALLOWED_ORIGINS.append(f'https://{VERCEL_URL}')
    # Permitir cualquier subdominio de vercel.app para previews
    CORS_ALLOWED_ORIGIN_REGEXES = [
        r'^https://.*\.vercel\.app$',
    ]

# HU-10 / CU27 / RF-31: recuperación de contraseña. Por defecto imprime el
# correo en la consola (útil en desarrollo sin credenciales SMTP reales);
# en producción, configurar EMAIL_HOST/EMAIL_HOST_USER/EMAIL_HOST_PASSWORD
# en el .env (SendGrid/Mailgun) y cambiar EMAIL_BACKEND a smtp.
# Recuperación de contraseña por correo SMTP (Gmail / Sendgrid)
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '').strip()
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '').strip()

if EMAIL_HOST_USER and EMAIL_HOST_PASSWORD:
    EMAIL_BACKEND = os.getenv('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
    EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
    EMAIL_PORT = int(os.getenv('EMAIL_PORT', '587'))
    EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'True') == 'True'
    DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', f'SIGEPSI <{EMAIL_HOST_USER}>')
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    EMAIL_HOST = ''
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    DEFAULT_FROM_EMAIL = 'no-reply@sigepsi.com'

# Token de recuperación válido por 5 minutos (criterio de aceptación HU-10a).
PASSWORD_RESET_TIMEOUT = 60 * 5

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

# Caché en memoria local — evita consultas repetitivas a Supabase
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'sigepsi-cache',
        'TIMEOUT': 10,  # 10 segundos por defecto
    }
}
