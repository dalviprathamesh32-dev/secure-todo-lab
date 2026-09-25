from pydantic import BaseModel , ConfigDict

class TaskCreate (BaseModel):
    task_name : str
    urgent : bool = False

class TaskResponse (BaseModel):
    id : int 
    task_name : str
    urgent : bool

    model_config = ConfigDict(from_attributes=True)

    