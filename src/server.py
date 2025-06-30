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
    name : str | None =None
    desc : str | None =None
    category : int | None =None
    priority : int | None =None
    date : str | None =None



@app.get("/")
def read_root():
    return {"Hello" : "World"}

@app.get("/tasks")
def fetchAll():
    out = tdl.serialize()
    return out

@app.post("/tasks")
def create(task: TaskModel):
    if ( task.name == None or task.category == None or task.priority == None or task.date == None ):
        raise HTTPException(status_code=400,detail="Requiered Field(s) Weren't Filled")
    if len(task.name)<3:
        raise HTTPException(status_code=400,detail="Task Title Too Small ! (min. 3)")
    t:Task = Task(
                    task.name,
                    Category(task.category),
                    Priority(task.priority),
                    task.date)
    if task.desc:
        t.setDesc(task.desc)
    tdl.add(t)
    return t.serialize()

@app.get("/tasks/{id}")
def fetch(id :int):
    out=tdl.fetch(id)
    if out:
        return out.serialize()
    else:
        raise HTTPException(status_code=404,detail="Task Not Found")
    

@app.put("/tasks/{id}")
def edit(id: int, task: TaskModel):
    out=tdl.fetch(id)
    if out:
        if(task.name):
            if len(task.name)<3:
                raise HTTPException(status_code=400,detail="Task Title Too Small ! (min. 3)")
            out.setName(task.name)
        if(task.category):
            out.setCategory(Category(task.category))
        if(task.priority):
            out.setPriority(Priority(task.priority))
        if(task.desc):
            out.setDesc(task.desc)
        if(task.date):
            out.setDate(task.date)
        return out.serialize()
    raise HTTPException(status_code=404,detail="Task Not Found")


@app.delete("/tasks/{id}")
def remove(id :int):
    out=tdl.popById(id)
    if (out):
        return out.serialize()
    raise HTTPException(status_code=404,detail="Task Not Found")

@app.get("/categories")
def fetchAllCategories():
    
    return Category.getList()