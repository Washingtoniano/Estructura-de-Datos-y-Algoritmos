from Lista_Encadenada import ListEnca
from  Lista_Secuencial import ListSecu
from ListaconCursor import LC
class menu():
    __swicher:None
    def __init__(self) -> None:
        self.__swicher= {
                        '1':self.opcion1,
                        '2':self.opcion2,
                        '3':self.opcion3
        }
    def opcion(self,op):
        fun=self.__swicher.get(op,lambda:print("Opcion invalida"))
        if op=='1' or op =='2' or op=='3':
            fun()
        else:
            fun()
    def opcion1(self):
        matriz1=ListSecu(2)
        matriz2=ListSecu(2)
        for i in range (2) :
            matriz1.insertar(ListSecu(2),i)
            matriz2.insertar(ListSecu(2),i)
        matriz1.Recorrer()
        matriz2.Recorrer()
        print("")
    def opcion2(self):
        pass
    def opcion3(self):
        pass