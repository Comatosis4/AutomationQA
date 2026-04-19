import os
import time

import psycopg2
import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="session")
def conn():

    time.sleep(5)  # чекати запуск postgres

    try:
        connection = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )

        print("Connected to the database successfully!")

        cursor = connection.cursor()

        # створюємо таблицю
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT
        )
        """)

        connection.commit()

    except Exception as error:
        pytest.fail(f"Error while connecting to PostgreSQL: {error}")

    yield connection

    connection.close()

    print("PostgreSQL connection is closed")


@pytest.fixture(scope="function")
def cursor_con(conn):

    cursor = conn.cursor()

    yield cursor, conn

    conn.commit()
    cursor.close()