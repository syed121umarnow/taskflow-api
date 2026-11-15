
import logging
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response, status

from app.dependencies import get_task_service
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from app.services.task_services import TaskService


logger = logging.getLogger(__name__)

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post(
    "",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_task(
    payload: TaskCreate,
    service: TaskService = Depends(get_task_service),
):
    task = service.create_task(
        title=payload.title,
        description=payload.description,
        status=payload.status,
    )

    logger.info("Task created: %s", task.id)

    return task


@router.get("", response_model=list[TaskResponse])
def get_all_tasks(
    service: TaskService = Depends(get_task_service),
):
    return service.get_all_tasks()


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: UUID,
    service: TaskService = Depends(get_task_service),
):
    task = service.get_task(task_id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    return task


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: UUID,
    payload: TaskUpdate,
    service: TaskService = Depends(get_task_service),
):
    task = service.update_task(
        task_id=task_id,
        title=payload.title,
        description=payload.description,
        status=payload.status,
    )

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    logger.info("Task updated: %s", task.id)

    return task


@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_task(
    task_id: UUID,
    service: TaskService = Depends(get_task_service),
):
    deleted = service.delete_task(task_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    logger.info("Task deleted: %s", task_id)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
