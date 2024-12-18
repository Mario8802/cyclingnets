# Използвай официалния Python образ
FROM python:3.11-slim

# Инсталиране на системни зависимости, необходими за Python пакети
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gcc \
    netcat-openbsd && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Задаване на работна директория в контейнера
WORKDIR /app

# Копиране на файла с изисквания
COPY requirements.txt /app/

# Инсталиране на Python зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копиране на всички проектни файлове
COPY . /app/

# Командата по подразбиране за стартиране на приложението с Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "bike_connect.wsgi:application"]
