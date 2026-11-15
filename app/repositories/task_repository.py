
from typing import Protocol
from uuid import UUID

from app.models.task import Task


class TaskRepository(Protocol):

    def create(self, task: Task) -> Task:
        ...

    def get_by_id(self, task_id: UUID) -> Task | None:
        ...

    def get_all(self) -> list[Task]:
        ...

    def update(self, task: Task) -> Task:
        ...

    def delete(self, task_id: UUID) -> bool:
        ...


class InMemoryTaskRepository:

    def __init__(self) -> None:
        self._tasks: dict[UUID, Task] = {}

    def create(self, task: Task) -> Task:
        self._tasks[task.id] = task
        return task

    def get_by_id(self, task_id: UUID) -> Task | None:
        return self._tasks.get(task_id)

    def get_all(self) -> list[Task]:
        return list(self._tasks.values())

    def update(self, task: Task) -> Task:
        self._tasks[task.id] = task
        return task

    def delete(self, task_id: UUID) -> bool:
        return self._tasks.pop(task_id, None) is not None
