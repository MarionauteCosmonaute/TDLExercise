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
    
    def serialize(self)->list[dict]:
        serializedtasklist :list[dict]=[]
        for t in self.toDoList: #serialize each element of the list
            serializedtasklist.append( t.serialize())
        return serializedtasklist
    
    def add(self, task : Task)->None:
        self.toDoList.append(task);

    def fetch(self, id:int)->dict:
        for t in self.toDoList:
            if t.id == id:
                return t.serialize()
        return {"error": "not found"}