import pytest
import allure


@allure.feature("Database connection")
@pytest.mark.db_test
def test_database_connection(conn):

    with allure.step("Check database connection exists"):
        assert conn is not None


@allure.feature("Database CRUD")
@pytest.mark.db_test
def test_data_insertion(cursor_con):

    cursor, conn = cursor_con

    with allure.step("Insert new user"):

        cursor.execute(
            "INSERT INTO users (name) VALUES ('John') RETURNING id"
        )

        user_id = cursor.fetchone()[0]

    with allure.step("Select inserted user"):

        cursor.execute(
            "SELECT name FROM users WHERE id = %s",
            (user_id,)
        )

        result = cursor.fetchone()

    with allure.step("Verify inserted data"):

        assert result is not None
        assert result[0] == "John"


@allure.feature("Database CRUD")
@pytest.mark.db_test
def test_update(cursor_con):

    cursor, conn = cursor_con

    with allure.step("Insert user for update"):

        cursor.execute(
            "INSERT INTO users (name) VALUES ('Mike') RETURNING id"
        )

        user_id = cursor.fetchone()[0]

    with allure.step("Update user name"):

        cursor.execute(
            "UPDATE users SET name='Updated' WHERE id=%s",
            (user_id,)
        )

    with allure.step("Verify updated data"):

        cursor.execute(
            "SELECT name FROM users WHERE id=%s",
            (user_id,)
        )

        result = cursor.fetchone()

        assert result[0] == "Updated"


@allure.feature("Database CRUD")
@pytest.mark.db_test
def test_delete(cursor_con):

    cursor, conn = cursor_con

    with allure.step("Insert user for delete"):

        cursor.execute(
            "INSERT INTO users (name) VALUES ('DeleteMe') RETURNING id"
        )

        user_id = cursor.fetchone()[0]

    with allure.step("Delete user"):

        cursor.execute(
            "DELETE FROM users WHERE id=%s",
            (user_id,)
        )

    with allure.step("Verify deletion"):

        cursor.execute(
            "SELECT name FROM users WHERE id=%s",
            (user_id,)
        )

        result = cursor.fetchone()

        assert result is None