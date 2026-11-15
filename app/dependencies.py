
from fastapi import Request

from app.repositories.task_repository import (
    InMemoryTaskRepository,
    TaskRepository,
)
from app.services.task_services import TaskService


def get_task_repository(request: Request) -> TaskRepository:
    return request.app.state.task_repository


def get_task_service(request: Request) -> TaskService:
    repository = get_task_repository(request)
    return TaskService(repository)
