from database.database import Database
from models.exception_case import ExceptionCase


class ExceptionCaseRepository:
    """Responsável pela persistência de ExceptionCase no SQLite."""

    def __init__(self, database: Database):
        self.database = database

    def create(self, case: ExceptionCase) -> ExceptionCase:
        with self.database.connect() as connection:
            cursor = connection.execute(
                """
                INSERT INTO exception_cases (
                    title,
                    description,
                    category,
                    priority,
                    status,
                    created_at,
                    updated_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    case.title,
                    case.description,
                    case.category,
                    case.priority,
                    case.status,
                    case.created_at,
                    case.updated_at,
                ),
            )

            case.id = cursor.lastrowid

        return case
