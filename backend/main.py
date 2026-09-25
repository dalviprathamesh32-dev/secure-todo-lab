from fastapi import FastAPI
from db import Base , engine
import models.tasks
from routes.tasks import router as task_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(task_router)

@app.get("/")
def get_health ():
    return {
        "status" : "Running",
        "App" : "Secure-todo-app"
    }
