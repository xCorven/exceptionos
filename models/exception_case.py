from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class ExceptionCase:
    """Representa uma exceção operacional registrada no ExceptionOS."""

    id: Optional[int] = None
    title: str = ""
    description: str = ""
    category: str = ""
    priority: str = "medium"
    status: str = "open"

    created_at: str = field(
        default_factory=lambda: datetime.now().isoformat(
            timespec="seconds"
        )
    )

    updated_at: str = field(
        default_factory=lambda: datetime.now().isoformat(
            timespec="seconds"
        )
    )
