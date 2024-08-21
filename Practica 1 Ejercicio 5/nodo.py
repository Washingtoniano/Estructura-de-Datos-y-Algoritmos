class nodo():
    __dato:object
    __sig:None
    def __init__(self,dato) -> None:
        self.__dato=dato
        self.__sig=None
    def setSiguiente(self,sig):
        self.__sig=sig
    def getSiguiente(self):
        return self.__sig
    def getDato(self):
        return self.__dato