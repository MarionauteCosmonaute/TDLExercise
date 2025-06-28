from  Task import Task
from Category import Category
from Priority import Priority
from datetime import datetime

class ToDoList:

    
    def __init__(self) -> None:
        self.toDoList: list[Task] = []
        
        
    def demo(self):
        self.toDoList = [Task(
                            "Etendre le linge",
                            Category.Personnel,
                            Priority.Haute,
                            "30/06/2025 13:30"),
                        Task(
                            "Faire les courses",
                            Category.Personnel,
                            Priority.Moyenne,
                            "01/07/2025 15:05"),
                        Task(
                            "Faire la vaisselle",
                            Category.Personnel,
                            Priority.Basse,
                            "02/05/2025 12:03")]

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
                
