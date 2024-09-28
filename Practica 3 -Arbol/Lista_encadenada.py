from caracter import caracter
from NodoArbol import nodo
#Lista der arboles
class Lista_enca():
    __primero:nodo
    __ultimo:nodo
    __cant:int
    
    def __init__(self):
        self.__primero=None
        self.__ultimo=None
        self.__cant=0
    def Vacio(self):
        return self.__cant==0
    def insertar(self,arbol):
        unnodo=nodo(arbol)
        if self.Vacio()==True:
            self.__primero=unnodo
            self.__ultimo=unnodo
        else:
            if self.__primero.getDato().getraiz().getDato().getFrecuencia()>unnodo.getDato().getraiz().getDato().getFrecuencia():
                unnodo.setSiguiente(self.__primero)
                self.__primero=unnodo
            else:
                aux=self.__primero
                ant=aux
                while aux!=None and aux.getDato().getraiz().getDato().getFrecuencia()<=unnodo.getDato().getraiz().getDato().getFrecuencia():
                    ant=aux
                    aux=aux.getSiguiente()
                if aux==None:
                    ant.setSiguiente(unnodo)
                    self.__ultimo=unnodo
                else:
                    unnodo.setSiguiente(ant.getSiguiente())
                    ant.setSiguiente(unnodo)

        self.__cant+=1
    def Uno(self):
        return self.__cant==1
    def Primero(self):
        if self.Vacio()!=True:
            return self.__primero

    def Suprimir(self,dato):
        borrado=None
        if self.Vacio()!=True:
            if self.__primero==dato:
                borrado=self.__primero
                self.__primero=self.__primero.getSiguiente()
                self.__cant-=1
            else:
                aux=self.__primero
                anterior=aux
                while aux!=None and aux!=dato:
                    anterior=aux
                    aux=aux.getSiguiente()
                if aux!=None:
                    borrado=aux
                    anterior.setSiguiente(aux.getSiguiente())
                    self.__cant-=1
            return borrado
        else:
            print("Lista vacia")
                    


