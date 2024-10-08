class nodo():
    __dato:int
    __sig:object

    def __init__(self,dato) -> None:
        self.__dato=dato
        self.__sig=None
    def getDato(self):
        return self.__dato
    def getSiguiente(self):
        return self.__sig
    def setSiguiente(self,sig):
        self.__sig=sig
    def setDato(self,Dato):
        self.__dato=Dato

    def insertar(self,colision):
        aux=self
        if colision.getDato()<self.getDato():
            colision.setSiguiente(aux.getSiguiente())
            self.setDato(colision.getDato())
            colision.setDato(aux.getDato())
            self.setSiguiente(colision)
            print("PAto")
        else:
            ant=aux
            while aux!=None and aux.getDato()<colision.getDato():
                ant=aux
                aux=aux.getSiguiente()
            colision.setSiguiente(ant.getSiguiente())
            ant.setSiguiente(colision)
            print("PAto")
    def Buscar(self,clave):
        aux=self
        encontrado=None
        while aux!=None and aux.getDato()!=clave:
            aux=aux.getSiguiente()
        if aux!=None:
            encontrado=aux.getDato()
        return encontrado
    def mostrar(self):
        aux=self
        print(aux)


    def __str__(self) -> str:
        return ("Dato: {} Sig: {}".format(self.__dato,self.__sig))