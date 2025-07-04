from fastapi import FastAPI,HTTPException
from ToDoList import ToDoList
from pydantic import BaseModel,ValidationError
from Task import Task
from Category import Category
from Priority import Priority
from fastapi.middleware.cors import CORSMiddleware

origins= ["http://localhost:5173","http://localhost:4173"]

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tdl:ToDoList = ToDoList()
tdl.demo()

class RequestFields(BaseModel):
    name : str 
    desc : str | None
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
def create(task: RequestFields):
    request:dict =task.model_dump()
    try:
        t:Task = Task(**request)
        tdl.add(t)
    except ValidationError as e:
        raise HTTPException(status_code=400,detail=e.json())
    return t.serialize()

@app.get("/tasks/{id}")
def fetch(id :int):
    out=tdl.fetch(id)
    if out:
        return out.serialize()
    else:
        raise HTTPException(status_code=404,detail="Task Not Found")
    

@app.put("/tasks/{id}")
def edit(id: int, task: RequestFields):
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