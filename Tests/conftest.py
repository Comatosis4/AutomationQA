import os
import time

# import psycopg2
import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="session")
def conn():

    retries = 10
    connection = None

    for i in range(retries):
        try:
            connection = psycopg2.connect(
                dbname=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT")
            )

            print("Connected to the database successfully!")
            break

        except Exception as error:
            print(f"Attempt {i + 1}: Database not ready, waiting...")
            time.sleep(3)

    if connection is None:
        pytest.fail("Could not connect to PostgreSQL after several attempts")

    yield connection

    connection.close()

    print("PostgreSQL connection is closed")


@pytest.fixture(scope="function")
def cursor_con(conn):

    cursor = conn.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS users ( 
                        id SERIAL PRIMARY KEY, 
                        name TEXT)
                """)

    conn.commit()

    yield cursor, conn

    conn.rollback()
    cursor.close()