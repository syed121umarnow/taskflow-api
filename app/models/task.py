
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from uuid import UUID, uuid4


class TaskStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


@dataclass
class Task:
    id: UUID
    title: str
    description: str | None
    status: TaskStatus
    created_at: datetime
    updated_at: datetime

    @classmethod
    def create(
        cls,
        title: str,
        description: str | None = None,
        status: TaskStatus = TaskStatus.PENDING,
    ) -> "Task":
        now = datetime.now().astimezone()

        return cls(
            id=uuid4(),
            title=title,
            description=description,
            status=status,
            created_at=now,
            updated_at=now,
        )
