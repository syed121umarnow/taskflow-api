
from datetime import datetime, timezone
from uuid import UUID

from app.models.task import Task, TaskStatus
from app.repositories.task_repository import TaskRepository


class TaskService:

    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    def create_task(
        self,
        title: str,
        description: str | None,
        status: TaskStatus,
    ) -> Task:
        task = Task.create(
            title=title,
            description=description,
            status=status,
        )

        return self.repository.create(task)

    def get_task(self, task_id: UUID) -> Task | None:
        return self.repository.get_by_id(task_id)

    def get_all_tasks(self) -> list[Task]:
        return self.repository.get_all()

    def update_task(
        self,
        task_id: UUID,
        title: str,
        description: str | None,
        status: TaskStatus,
    ) -> Task | None:
        existing_task = self.repository.get_by_id(task_id)

        if existing_task is None:
            return None

        updated_task = Task(
            id=existing_task.id,
            title=title,
            description=description,
            status=status,
            created_at=existing_task.created_at,
            updated_at=datetime.now(timezone.utc),
        )

        return self.repository.update(updated_task)

    def delete_task(self, task_id: UUID) -> bool:
        return self.repository.delete(task_id)
