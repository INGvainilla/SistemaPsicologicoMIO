#!/bin/sh
set -e

# Si PORT no está definido, usar 8000 por defecto
PORT="${PORT:-8000}"

echo "=========================================="
echo "Iniciando SIGEPSI Backend en puerto: $PORT"
echo "=========================================="

# Iniciar gunicorn
exec gunicorn sigepsi.wsgi:application \
    --bind "0.0.0.0:$PORT" \
    --workers 3 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile -
