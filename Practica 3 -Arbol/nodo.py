class nodo():
    __dato:int
    __izquierda:object
    __derecha:object

    def __init__(self,dato) -> None:
        self.__dato=dato
        self.__izquierda=None
        self.__derecha=None

    def setIzquierda(self,iz):
        self.__izquierda=iz

    def setDerecha(self,de):
        self.__derecha=de

    def getDato(self):
        return self.__dato
    
    def getIzquierda(self):
        return self.__izquierda
    
    def getDerecha(self):
        return self.__derecha