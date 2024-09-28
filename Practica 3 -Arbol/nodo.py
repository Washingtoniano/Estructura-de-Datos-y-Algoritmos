class nodo():
    __dato:object
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
    def getGrado(self):
        grado=0
        if self.__derecha!=None:
            grado+=1
        if self.__izquierda!=None:
            grado+=1
        return grado