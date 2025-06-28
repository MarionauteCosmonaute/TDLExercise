from Category import Category
from Priority import Priority
import itertools
from datetime import datetime


class Task:
    """
    Classe modélisant les tâches dans la to do list
    """
    name : str
    desc : str 
    category : Category
    priority : Priority
    date : datetime

    #id autoincrémental
    id_gen = itertools.count()


    def __init__(self,
                    name: str ,
                    category: Category,
                    priority: Priority,
                    date:str ) -> None:
        """
        
        Constructeur de Task, contient tous les champs obligatoires d'une tache
        
        *name* : titre de la tache
        *category* : catégorie de la tache
        *priority* : priorité de la tache
        *date* : échéance de la tache
        
        """
        self.id= next(self.id_gen)
        self.name=name
        self.category=category
        self.priority=priority
        self.date=datetime.strptime(date,"%d/%m/%Y %H:%M")
        
    
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
        out = {
                    "id" : self.id,
                    "name" : self.name,
                    "category" : self.category.name,
                    "priority" :self.priority.name,
                    "date" : self.date.strftime("%d/%m/%Y %H:%M")
                }
        #attribut facultatif, ajout de celui ci que s'il existe
        if (hasattr(self,"desc")):
            out["desc"]=self.desc
        return out

    def setName(self,name: str) -> None:
        self.name=name

    def setCategory(self,category:Category)->None:
        self.category=category
    
    def setPriority(self,priority:Priority)->None:
        self.priority=priority

    def setDate(self,date:str)->None:
        self.date=datetime.strptime(date,"%d/%m/%Y %H:%M")
