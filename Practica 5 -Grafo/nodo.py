class nodo():
    __valor:int
    __sig:object
    def __init__(self,n) -> None:
        self.__valor=n
        self.__sig=None
    def setDato(self,da):
        self.__valor=da
    def setSig(self,sig):
        self.__sig=sig
    def getDato(self):
        return self.__valor
    def getSig(self):
        return self.__sig