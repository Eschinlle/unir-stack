#!/bin/bash

# Script para iniciar Unir Stack con Docker Compose

echo "🚀 Iniciando Unir Stack..."

# Verificar si existe el archivo .env
if [ ! -f .env ]; then
    echo "📝 Creando archivo .env desde .env.example..."
    cp .env.example .env
fi

# Detener contenedores previos si existen
echo "🛑 Deteniendo contenedores previos..."
docker-compose down

# Construir imágenes
echo "🔨 Construyendo imágenes Docker..."
docker-compose build

# Iniciar servicios
echo "🚀 Iniciando servicios..."
docker-compose up -d

# Esperar a que la base de datos esté lista
echo "⏳ Esperando a que la base de datos esté lista..."
sleep 5

# Ejecutar migraciones
echo "🔄 Ejecutando migraciones de base de datos..."
docker-compose exec backend bash -c "cd /app && alembic upgrade head"

# Mostrar logs
echo "✅ Unir Stack está listo!"
echo ""
echo "📌 URLs:"
echo "   - Frontend: http://localhost:3000"
echo "   - Backend API: http://localhost:8000"
echo "   - Documentación API: http://localhost:8000/docs"
echo ""
echo "📋 Comandos útiles:"
echo "   - Ver logs: docker-compose logs -f"
echo "   - Detener: docker-compose down"
echo "   - Reiniciar: docker-compose restart"
echo ""

# Seguir los logs
docker-compose logs -f