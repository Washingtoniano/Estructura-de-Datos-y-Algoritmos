#Esta clase sustituye al nodo
#Este nuevo nodo hara de arbol
class caracter():
    __siguiente:object
    __carac:str
    __frecuencia:int
    __codigo:list
    __izquierda:object
    __derecha:object

    def __init__(self,ca):
        self.__carac=ca
        self.__frecuencia=0
        self.__codigo=[]
        self.__siguiente=None
        self.__izquierda=None
        self.__derecha=None
    def getCodigo(self):
        return (self.__codigo)
    def getFrecuencia(self):
        return (self.__frecuencia)
    def getDato(self):
        return self.__carac
    def getDerecha(self):
        return self.__derecha
    def getIzquierda(self):
        return self.__izquierda
    def getSiguiente(self):
        return self.__siguiente
    def setSiguiente(self,sig):
        self.__siguiente=sig
    def setFrecuencia(self,d):
        self.__frecuencia=d
    def setCodigo(self,bi):
        self.__codigo.append(bi)
    def setDerecha(self,der):
        self.__derecha=der
    def setIzquierda(self,iz):
        self.__izquierda=iz
    def mostrar(self):
        d=None
        for i in range (len(self.__codigo)):
            if d==None:
                d=self.__codigo[i]
            else:
                d+=self.__codigo[i]
        print("Caracter:{} Frecuencia {} Codigo {}".format(self.getDato(),self.getFrecuencia(),d))


    def __str__(self) -> str:
        d=None
        for i in range (len(self.__codigo)):
            if d==None:
                d=self.__codigo[i]
            else:
                d+=self.__codigo[i]
        return("Caracter:{} Frecuencia {} Codigo {}".format(self.getDato(),self.getFrecuencia(),d))
    def __eq__(self, other) -> bool:
        if type (self)==caracter and type (other)==caracter:
            return self.getDato()==other.getDato() and self.getFrecuencia()==other.getFrecuencia()
    