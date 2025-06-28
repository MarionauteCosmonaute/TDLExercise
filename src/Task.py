from Category import Category
from Priority import Priority
import itertools
import datetime


class Task:
    """
    Classe modélisant les tâches dans la to do list
    """

    #id autoincrémental
    id_gen = itertools.count()


    def __init__(self,
                    name: str ,
                    category: Category,
                    priority: Priority,
                    date:datetime.datetime ) -> None:
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
        self.date=date
        
    
    def addDesc(self,
                description: str):
        """
        Permet d'ajouter le champ facultatif correspondant à la description
        """
        self.desc=description
    
    def serialize(self):
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
    
