import psycopg2
import os

# Параметры подключения к базе данных PostgreSQL
hostname = os.getenv('DB_HOST')  # или IP адрес сервера БД
database = os.getenv('DB_NAME')
username = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
port_id = os.getenv('DB_PORT')  # стандартный порт PostgreSQL

# Подключение к базе данных
conn = psycopg2.connect(
    host=hostname,
    dbname=database,
    user=username,
    password=password,
    port=port_id
)

# Создание курсора
cursor = conn.cursor()

# SQL-запрос
sql_query = "SELECT * FROM newtable LIMIT 10"

try:
    # Выполнение запроса
    cursor.execute(sql_query)

    # Получение результатов
    rows = cursor.fetchall()

    # Вывод результатов
    for row in rows:
        print(row)

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Закрытие курсора и соединения
    cursor.close()
    conn.close()