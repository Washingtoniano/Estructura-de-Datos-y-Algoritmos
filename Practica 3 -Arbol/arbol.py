from nodo import nodo
class arbol():
    __raiz:nodo
    def __init__(self) -> None:
        self.__raiz=None

    def insertar(self,arbol,dato):
        unnodo=nodo(dato)
        if arbol==None:
            arbol=unnodo
        elif arbol.getDato()==unnodo.getDato():
            print("Dato ya ingresado")
        elif arbol.getDato()>unnodo.getDato():
            self.recur(arbol.getIzquierda(),dato)
        elif arbol.getDato()<unnodo.getDato():
            self.recur(arbol.getDerecha(),dato)
    def getraiz(self):
        return self.__raiz
        
    def suprimir(self,arbol,dato):
        if arbol==None:
            print("No hay dato")
        if arbol.getDato()>dato:
            self.suprimir(arbol.getIzquierda(),dato)
