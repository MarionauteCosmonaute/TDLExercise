from  Task import Task
from Category import Category
from Priority import Priority
from pydantic import ValidationError

class ToDoList:

    
    def __init__(self) -> None:
        self.toDoList: list[Task] = []
        
        
    def demo(self):
        """Ajoute des éléments à la todolist à des fins de débug ou démo"""
        t0:dict={
            'name' :        "Laver le linge",
            'category':     Category.Personnel.value,
            'priority':     Priority.Moyenne.value,
            'date':         "30/07/2025 9:30"
        }
        t1:dict={
            'name' :        "Etendre le linge",
            'category':     Category.Personnel.value,
            'priority':     Priority.Basse.value,
            'date':         "30/07/2025 13:30"
        }
        t2: dict= {
            'name' :        "Promenener le chien",
            'category':     Category.Personnel.value,
            'priority':     Priority.Moyenne.value,
            'date':         "30/06/2025 8:30"
        }
        t3: dict={
            'name' :        "Préparer le repas de la semaine",
            'category':     Category.Personnel.value,
            'priority':     Priority.Haute.value,
            'date':         "07/07/2025 8:30",
            'desc':         "Lundi : Linguine Carbonara, Mardi : Sauté de Boeuf laquée, Mercredi: Lasagnes d'épinards, Jeudi: Curry de Légumes,Vendredi : Gratin Dauphinois, Samedi: Ramen, Dimanche: Gnocchis de Brocolis avec Pesto Rouge "
        }
        t4: dict={
            'name' :        "Démo To Do List",
            'category':     Category.Professionnel.value,
            'priority':     Priority.Haute.value,
            'date':         "04/07/2025 17:00",
            'desc':         "Ne pas trop stresser :)"
        }
        t5: dict={
            'name' :        "Rendez-vous avec le médecin",
            'category':     Category.Medical.value,
            'priority':     Priority.Basse.value,
            'date':         "10/07/2025 10:00",
            'desc':         "Vérification mensuelle de santé"
        }
        t6: dict={
            'name' :        "Réunion d'équipe",
            'category':     Category.Professionnel.value,
            'priority':     Priority.Haute.value,
            'date':         "05/07/2025 14:00",
            'desc':         "Discussion des objectifs du trimestre"
        }
        t7:dict={
            'name' :        "Soirée cinéma entre ami.es",
            'category':     Category.Loisir.value,
            'priority':     Priority.Moyenne.value,
            'date':         "06/07/2025 20:00",
            'desc':         "Acheter BluRay/VOD : Le Seigneur des Anneaux: La Communauté de l'Anneau version longue, Le Seigneur des Anneaux: Les Deux Tours version longue, Le Seigneur des Anneaux: Le Retour du Roi version longue"
        }
        try:
            T0:Task=Task(**t0)
            T1:Task=Task(**t1)
            T2:Task=Task(**t2)
            T3:Task=Task(**t3)
            T4:Task=Task(**t4)
            T5:Task=Task(**t5)
            T6:Task=Task(**t6)
            T7:Task=Task(**t7)

            self.toDoList.append(T0)  
            self.toDoList.append(T1)
            self.toDoList.append(T2)
            self.toDoList.append(T3)
            self.toDoList.append(T4)
            self.toDoList.append(T5)
            self.toDoList.append(T6)
            self.toDoList.append(T7)
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
                
