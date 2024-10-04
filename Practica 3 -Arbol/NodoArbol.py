#No sirve eliminar
from arbol import arbol
class nodo():
    __dato:arbol
    __siguiente:object
    def __init__(self,dato) -> None:
        self.__dato=dato
        self.__siguiente=None
    def getDato(self):
        return self.__dato
    def setSiguiente(self,sig):
        self.__siguiente =sig
    def getSiguiente(self):
        return self.__siguiente