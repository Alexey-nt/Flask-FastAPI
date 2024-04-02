"""
Создать API для управления списком задач. Приложение должно иметь
возможность создавать, обновлять, удалять и получать список задач.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс Task с полями id, title, description и status.
Создайте список tasks для хранения задач.
Создайте маршрут для получения списка задач (метод GET).
Создайте маршрут для создания новой задачи (метод POST).
Создайте маршрут для обновления задачи (метод PUT).
Создайте маршрут для удаления задачи (метод DELETE).
Реализуйте валидацию данных запроса и ответа.
"""
import uvicorn
from fastapi import FastAPI

from typing import Optional
from pydantic import BaseModel
from random import choice

app = FastAPI()


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: str


statuses = ["to do", "in progress", "done"]
tasks = []
for i in range(1, 6):
    id = i
    title = "name_" + str(i)
    description = "description_" + str(i) * 3
    status = choice(statuses)
    data = {"id": id, "title": title, "description": description, "status": status}
    task = Task(**data)
    tasks.append(task)


@app.get("/")
async def root():
    return {"message": "Hello world"}


@app.get("/data/")
async def receive():
    return {"task_list": tasks}


@app.post("/tasks/")
async def create_task(task: Task):
    tasks.append(task)
    return task


@app.put("/tasks/{task_id}")
async def updating(task_id: int, task: Task):
    for index, t in enumerate(tasks):
        if t.id == task_id:
            tasks[index] = task
    return task


@app.delete("/task/{task_id}")
async def delete_data(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
    return {"task_id": task_id}


if __name__ == '__main__':
    uvicorn.run("task_1:app", host="127.0.0.1", port=8000)
