from nodo import nodo
#Esta clase sustituye al nodo
class caracter():
    __carac:str
    __frecuencia:int
    __codigo:list
    __siguiente:object

    def __init__(self,ca):
        self.__carac=ca
        self.__frecuencia=0
        self.__codigo=[]
        self.__siguiente=None
    def getCodigo(self):
        return (self.__codigo)
    def getFrecuencia(self):
        return (self.__frecuencia)
    def getCaracter(self):
        return (self.__carac)
    def getSiguiente(self):
        return self.__siguiente
    def setFrecuencia(self,d):
        self.__frecuencia=d
    def setCodigo(self,bi):
        self.__codigo.append(bi)
    def setSiguiente(self,sig):
        self.__siguiente=sig
    def __lt__(self,other):
        b=None
        if type(other)==nodo:
            n=other.getDato()
            b=self.getFrecuencia()<n.getFrecuencia()
        elif type(other)==str:
            b=self.getCaracter()<other
        else:
            b=self.getFrecuencia()<other.getFrecuencia()
        return b
    def __gt__(self,other):
        b=None
        if type(other)==nodo:
            n=other.getDato()
            b=self.getFrecuencia()>n.getFrecuencia()
        elif type(other)==str:
            b=self.getCaracter()>other
        else:

            b=self.getFrecuencia()>other.getFrecuencia()
        return b

    def __add__(self,other):
        b=None
        if type(other)==nodo:
            n=other.getDato()
            b=self.getCaracter()+n.getCaracter()
        else:
            b=(self.getCaracter()+other.getCaracter())
        return b
    def __str__(self) -> str:
        d=None
        for i in range (len(self.__codigo)):
            if d==None:
                d=self.__codigo[i]
            else:
                d+=self.__codigo[i]
        return("Caracter:{} Frecuencia {} Codigo {}".format(self.getCaracter(),self.getFrecuencia(),d))
    def __eq__(self, other) -> bool:
        return self.getCaracter()==other.getCaracter() and self.getFrecuencia()==other.getFrecuencia()