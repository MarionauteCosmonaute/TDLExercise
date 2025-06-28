from fastapi import FastAPI,HTTPException
from ToDoList import ToDoList
from pydantic import BaseModel
from Task import Task
from Category import Category
from Priority import Priority
from datetime import datetime

app=FastAPI()

tdl:ToDoList = ToDoList()
tdl.demo()

class TaskModel(BaseModel):
    name : str
    desc : str | None =None
    category : int
    priority : int
    date : str



@app.get("/")
def read_root():
    return {"Hello" : "World"}

@app.get("/tasks")
def fetchAll():
    out = tdl.serialize()
    return out

@app.post("/tasks")
def create(task: TaskModel):
    if len(task.name)<3:
        #jsp exactement quel code de status mettre
        raise HTTPException(status_code=426,detail="Task Title Too Small ! (min. 3)")
    t:Task = Task(
                    task.name,
                    Category(task.category),
                    Priority(task.priority),
                    datetime.strptime(task.date,"%d/%m/%Y %H:%M"))
    if task.desc:
        t.addDesc(task.desc)
    tdl.add(t)
    return t.serialize()

@app.get("/tasks/{id}")
def fetch(id :int):
    out=tdl.fetch(id)
    if out["error"]:
        raise HTTPException(status_code=404,detail=out["error"])
    return out

@app.put("/tasks/{id}")
def edit(id: int):
    #TODO: implement edit

    return {}

@app.delete("/tasks/{id}")
def remove(id :int):
    #TODO: implement remove
    return {}

@app.get("/categories")
def fetchAllCategories():
    #TODO: implement fetchAllCategories
    return {}