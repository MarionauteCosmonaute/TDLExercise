from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def read_root():
    return {"Hello" : "World"}

@app.get("/tasks")
def fetchAll():
    #TODO: implement fetchAll
    return {}

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