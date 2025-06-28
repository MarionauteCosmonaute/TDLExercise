from fastapi import FastAPI
from  Task import Task
from Category import Category
from Priority import Priority
from datetime import datetime
import json

app=FastAPI()

tasklist: list[Task] = [Task(
                            "Etendre le linge",
                            Category.Personnel,
                            Priority.Haute,
                            datetime(year=2025,month=6,day=30,hour=12,minute=30)),
                        Task(
                            "Faire les courses",
                            Category.Personnel,
                            Priority.Moyenne,
                            datetime(year=2025,month=7,day=1,hour=10,minute=30)),
                        Task(
                            "Faire la vaisselle",
                            Category.Personnel,
                            Priority.Basse,
                            datetime(year=2025,month=6,day=30,hour=12,minute=45))]

@app.get("/")
def read_root():
    return {"Hello" : "World"}

@app.get("/tasks")
def fetchAll():
    serializedtasklist :list[dict]=[]
    for t in tasklist: 
        serializedtasklist.append( t.serialize())
    return serializedtasklist

@app.post("/tasks")
def create():
     #TODO: implement create
    return {}

@app.get("/tasks/{id}")
def fetch(id :int):
     #TODO: implement fetch
    return {}

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