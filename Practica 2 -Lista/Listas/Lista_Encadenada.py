from nodo import Nodo
class ListEnca():
    __comienzo:Nodo
    __cant:int
    __ultimo:Nodo
    
    def __init__(self) -> None:
        self.__comienzo=None
        self.__cant=0
        self.__ultimo=None
    def Vacio(self):
        return self.__cant==0
    def insertarPorPosicion(self,dato,pos=0):
        if self.Vacio():
            unnodo=Nodo(dato)
            self.__comienzo=unnodo
            self.__ultimo=unnodo
            self.__cant+=1
        elif pos==self.__cant:
            aux=self.__comienzo
            while aux.getSiguiente()!=None:
                aux=aux.getSiguiente()
            aux.setSiguiente(unnodo)
            self.__ultimo=unnodo
            self.__cant+=1
        elif pos==0:
            unnodo.setSiguiente(self.__comienzo)
            self.__comienzo=unnodo
            self.__cant+=1
        elif pos<self.__cant:
            unnodo=Nodo(dato)
            aux=self.__comienzo
            for i in range(pos-1):
                aux=aux.getSiguiente()
            unnodo.setSiguiente(aux.getSiguiente())
            aux.setSiguiente(unnodo)
            self.__cant+=1
        else:
            print("Error No se puede insertar")
    




