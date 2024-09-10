class Nodo():
    __dato:object
    __siguiente:object
    def __init__(self,dato) -> None:
        self.__siguiente=None
        self.__dato=dato

    def getDato(self):
        return self.__dato
    
    def setSiguiente(self,sig):
        self.__siguiente=sig
    def getSiguiente(self):
        return self.__siguiente