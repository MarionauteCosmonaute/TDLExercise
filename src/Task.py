from Category import Category
from Priority import Priority
from pydantic import BaseModel,field_validator,field_serializer
from typing import ClassVar
import itertools
from datetime import datetime


class Task(BaseModel):
    """
    Classe modélisant les tâches dans la to do list
    """
    id : int
    name : str
    desc : str | None
    category : int
    priority : int
    date : datetime
    id_gen : ClassVar

    #id autoincrémental
    id_gen = itertools.count()


    def __init__(self,
                    name: str ,
                    category: int,
                    priority: int,
                    date:str,
                    desc :str |None =None ) -> None:
        """
        
        Constructeur de Task, contient tous les champs obligatoires d'une tache
        
        *name* : titre de la tache
        *category* : catégorie de la tache
        *priority* : priorité de la tache
        *date* : échéance de la tache
        
        """
        super().__init__(id=next(self.id_gen),name=name,category=category,priority=priority,date=date,desc=desc)
        
    
    def setDesc(self,
                description: str):
        """
        Permet d'ajouter/modifier le champ facultatif correspondant à la description
        """
        self.desc=description
    
    def serialize(self) -> dict:
        """
        renvoie une représentation de l'objet sous forme de dictionnaire afin de le rendre serializable
        """
        out=self.model_dump();
        return out

    def setName(self,name: str) -> None:
        self.name=name

    def setCategory(self,category:Category)->None:
        self.category=category.value
    
    def setPriority(self,priority:Priority)->None:
        self.priority=priority.value

    def setDate(self,date:str)->None:
        self.date=datetime.strptime(date,"%d/%m/%Y %H:%M")

    @field_validator('date', mode='before')
    def parse_date(cls, value):
        if isinstance(value, str):
            return datetime.strptime(value, "%d/%m/%Y %H:%M")
        return value
    
    def model_dump(self):
        dump=super().model_dump()
        dump['date']=self.date.strftime("%d/%m/%Y %H:%M")
        return dump
