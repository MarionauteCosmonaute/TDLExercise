from enum import Enum

class Category(Enum):
    Personnel =0
    Professionnel =1
    Medical =2
    Loisir =3

    @classmethod
    def getList(cls)->list[str]:
        return list(map(lambda c: c.name, cls))

