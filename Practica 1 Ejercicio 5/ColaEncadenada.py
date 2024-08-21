from nodo import nodo
class ColaEnca():
    __comienzo:None
    __cant:int
    __ultimo:None

    def __init__(self) -> None:
        self.__comienzo=None
        self.__cant=0
        self.__ultimo=None

    def insertar(self,dato):
        unnodo=nodo(dato)
        if self.__comienzo==None:
            self.__comienzo=unnodo
            self.__ultimo=unnodo
        else:
            aux=self.__comienzo
            while aux.getSiguiente()==None:
                aux=aux.getSiguiente()
            aux.setSiguiente(unnodo)
            self.__ultimo=unnodo

        self.__cant+=1
    def vacio(self):
        return self.__comienzo==None
    
    def suprimir(self):
        d=None
        if self.vacio()!=True:
            d=self.__comienzo.getDato()
            self.__comienzo=self.__comienzo.getSiguiente()
            self.__cant-=1
        return d
    
    def recorrer(self):
        aux=self.__comienzo
        while aux!=None:
            print(aux.getDato())
            aux=aux.getSiguiente()
        print("Se recorrio la cola")

