from nodo import nodo
class arbol():
    __raiz:nodo
    def __init__(self) -> None:
        self.__raiz=None
    def vacio(self):
        return self.__raiz==None
    def insertar(self,arbol,dato):
        unnodo=nodo(dato)
        if self.vacio()==True:
            self.__raiz=unnodo
        elif arbol.getDato()==dato:
            print("Dato ya ingresado")
        elif arbol.getDato()>dato:
            if arbol.getIzquierda()==None:
                arbol.setIzquierda(unnodo)
            else:
                self.insertar(arbol.getIzquierda(),dato)
        elif arbol.getDato()<dato:
            if arbol.getDerecha()==None:
                arbol.setDerecha(unnodo)
            else:
                self.insertar(arbol.getDerecha(),dato)
    def getraiz(self):
        return self.__raiz
        
    def suprimir(self,arbol,dato):
        if arbol==None:
            print("No hay dato")
        else:
            d=arbol.getDato()
            if d>dato:
                
                if arbol.getIzquierda() !=None and arbol.getIzquierda().getDato()!=dato:
                    self.suprimir(arbol.getIzquierda(),dato)
                else:
                    arbol.setIzquierda(None)
            elif d<dato:
                if arbol.getDerecha()!=None and arbol.getDerecha().getDato()!=dato:
                    self.suprimir(arbol.getDerecha(),dato)
                else:
                    arbol.setDerecha(None)
    def Buscar(self,arbol,dato):
        #Se pueden borrar el primer if y el print
        a=False
        if arbol==None:
            print("Dato inexistente")
        elif arbol.getDato()==dato:
            a=True
        elif arbol.getDato()<dato:
            a=self.Buscar(arbol.getDerecha(),dato)
        elif arbol.getDato()>dato:
            a=self.Buscar(arbol.getIzquierda(),dato)
        return a
    def preorden(self,arbol):
        if arbol!=None:
            print(arbol.getDato())

            self.preorden(arbol.getIzquierda())

            self.preorden(arbol.getDerecha())
    def postorden(self,arbol):
        if arbol!=None:

            self.postorden(arbol.getIzquierda())
            self.postorden(arbol.getDerecha())
            print(arbol.getDato())


    def inorden(self,arbol):
        if arbol!=None:
            self.inorden(arbol.getIzquierda())

            print(arbol.getDato())
            self.inorden(arbol.getDerecha())





            
