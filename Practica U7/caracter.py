#Esta clase sustituye al nodo
#Este nuevo nodo hara de arbol
class caracter():
    __siguiente:object
    __carac:str
    __frecuencia:int
    __codigo:str
    __izquierda:object
    __derecha:object

    def __init__(self,ca):
        self.__carac=ca
        self.__frecuencia=0
        self.__codigo=None
        self.__siguiente=None
        self.__izquierda=None
        self.__derecha=None
    def getCodigo(self):
        h=str(self.__codigo)
        #for i in range(1,len(self.__codigo)):
        #    h+=str(self.__codigo[i])
        return (h)
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
        bi=str(bi)
        if self.__codigo==None:
            self.__codigo=bi
        else:
            self.__codigo+=bi
        #self.__codigo.append(bi)
        #print(bi)
        #print(self.__codigo[0])
    def setDerecha(self,der):
        self.__derecha=der
    def setIzquierda(self,iz):
        self.__izquierda=iz
    def mostrar(self):
        cod=None
        li=self.getCodigo()
        lon=len(li)
        i=0
        if lon>0:
            cod=str(li[i])
            i+=1
            while i <lon:
                cod=cod+str(li[i])
                i+=1
        print("\nCaracter:{} Frecuencia {} Codigo:{}".format(self.getDato(),self.getFrecuencia(),cod))
    def grado(self):
        grado=0
        if self.__derecha!=None:
            grado+=1
        if self.__izquierda!=None:
            grado+=1
        return grado


    def __str__(self) -> str:
        d=None
        for i in range (len(self.__codigo)):
            if d==None:
                d=self.__codigo[i]
            else:
                d+=self.__codigo[i]
        return("Caracter:{} Frecuencia {} Codigo {}".format(self.getDato(),self.getFrecuencia(),d))
    def __eq__(self, other) -> bool:
        h=False
        if type (self)==caracter and type (other)==caracter:
            h= self.getDato()==other.getDato() and self.getFrecuencia()==other.getFrecuencia()
        elif type(self)==caracter and type(other)==str:
            h=self.getDato()==other
        return h

    