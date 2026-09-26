from fastapi import HTTPException , APIRouter , Depends , status
from db import get_db
from models.tasks import tasks as Task
from schemas.tasks import TaskCreate , TaskResponse
from sqlalchemy.orm import Session

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post(
    "/", response_model=TaskResponse , status_code=status.HTTP_201_CREATED
)
def create_task(task_data : TaskCreate, db : Session = Depends(get_db)):
    new_task = Task(task_name=task_data.task_name,urgent=task_data.urgent)

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


@router.get(
    "/" , response_model=list[TaskResponse]
)
def get_all_tasks (db : Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks


@router.delete(
    "/{task_id}" , status_code=status.HTTP_200_OK
)
def delete_task (task_id: int , db : Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= f"Task with id: {task_id} not found"
        )
    db.delete(task)
    db.commit()

    return {
        "status" : f"Task id: {task_id} gets deleted successfully"
    }

