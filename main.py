from typing import List

from fastapi import FastAPI

from schemas.task import Task

app = FastAPI(
    title="MyTaskAPI"
)

tasks = []


@app.get("/")
def hello():
    return "Niggers"


@app.post("/tasks", response_model=Task)
def create_task(task: List[Task]):
    tasks.extend(task)
    return {"status": 200, "data": tasks}
