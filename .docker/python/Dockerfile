FROM python:3.12.1-bookworm

# Install system dependencies required for psycopg2
RUN apt-get update && apt-get install -y \
    postgresql \
    postgresql-contrib \
    libpq-dev \
    gcc \
    python3-dev  # if you are using Python 3


# Copy the requirements.txt file into the Docker image
COPY ./../../requirements.txt /requirements.txt

# Установка зависимостей
RUN pip install -r /requirements.txt

# Команда для запуска контейнера
CMD ["tail", "-f", "/dev/null"]

# Установка рабочего каталога в контейнере
WORKDIR /app