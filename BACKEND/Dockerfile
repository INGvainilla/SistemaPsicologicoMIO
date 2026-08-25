FROM python:3.12-slim

# Evitar buffering de logs y bytecode
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8000

WORKDIR /app

# Instalar dependencias del sistema necesarias para PostgreSQL y compilación
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar todo el código del backend
COPY . /app/

# Exponer puerto
EXPOSE 8000

# Comando de inicio: collectstatic + registrar dominio + gunicorn
CMD sh -c "python manage.py collectstatic --noinput && python add_production_domain.py && gunicorn sigepsi.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 3"
