FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Permisos de ejecución para el script de inicio
RUN chmod +x /app/start.sh

# Ejecutar collectstatic durante la fase de build
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["/app/start.sh"]
