from  Task import Task
from Category import Category
from Priority import Priority
from datetime import datetime
from pydantic import ValidationError
class ToDoList:

    
    def __init__(self) -> None:
        self.toDoList: list[Task] = []
        
        
    def demo(self):
        t1:dict={
            'name' :        "Etendre le linge",
            'category':     Category.Personnel.value,
            'priority':     Priority.Haute.value,
            'date':         "30/06/2025 13:30"
        }
        try:
            T1:Task=Task(**t1)
            self.toDoList.append(T1)
            print(T1.model_dump())
        except ValidationError as e:
            print(e.errors())
        

    def serialize(self)->list[dict]:
        serializedtasklist :list[dict]=[]
        for t in self.toDoList: #serialize each element of the list
            serializedtasklist.append( t.serialize())
        return serializedtasklist

    def add(self, task : Task)->None:
        self.toDoList.append(task);

    def fetch(self, id:int)->Task | None:
        for t in self.toDoList:
            if t.id == id:
                return t
    
    def popById(self, id:int)->Task | None:
        for i in range(len(self.toDoList)):
            if self.toDoList[i].id==id:
                return self.toDoList.pop(i)
                
