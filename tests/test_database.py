import sqlite3

from database.database import Database


def test_initialize_cria_tabela_exception_cases(tmp_path):
    db_path = tmp_path / "test.db"

    database = Database(db_path)
    database.initialize()

    with sqlite3.connect(db_path) as connection:
        cursor = connection.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
              AND name = 'exception_cases'
            """
        )

        table = cursor.fetchone()

    assert table is not None
    assert table[0] == "exception_cases"

