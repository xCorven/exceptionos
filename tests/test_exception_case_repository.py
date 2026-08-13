import sqlite3

from database.database import Database
from models.exception_case import ExceptionCase
from repositories.exception_case_repository import ExceptionCaseRepository


def test_create_salva_exception_case_no_banco(tmp_path):
    db_path = tmp_path / "test.db"

    database = Database(db_path)
    database.initialize()

    repository = ExceptionCaseRepository(database)

    case = ExceptionCase(
        title="Nota fiscal divergente",
        description="Valor diferente do pedido",
        category="financeiro",
        priority="high",
    )

    created_case = repository.create(case)

    assert created_case.id is not None
    assert created_case.id == 1

    with sqlite3.connect(db_path) as connection:
        row = connection.execute(
            """
            SELECT
                id,
                title,
                description,
                category,
                priority,
                status
            FROM exception_cases
            WHERE id = ?
            """,
            (created_case.id,),
        ).fetchone()

    assert row is not None
    assert row[0] == created_case.id
    assert row[1] == "Nota fiscal divergente"
    assert row[2] == "Valor diferente do pedido"
    assert row[3] == "financeiro"
    assert row[4] == "high"
    assert row[5] == "open"
