from nodo import nodo

class ColaEnca():
    __comienzo:None
    __cant:int
    __ultimo = None

    def __init__(self):
        self.__comienzo = None
        self.__cant = 0
        self.__ultimo = None

    def insertar(self,dato):

        unNodo = nodo(dato)

        if self.__comienzo == None:
            self.__comienzo = unNodo
            self.__ultimo = unNodo

        else:
            aux = self.__comienzo
            while aux.getSig() != None:
                  aux = aux.getSig()

            aux.setSiguiente(unNodo)
            self.__ultimo = unNodo
        self.__cant+= 1


    def vacio(self):
        return self.__comienzo == None   

    def suprimir(self):

        #print("\n Se suprimio el primer elemento ")

        if self.vacio() != True:
            d = self.__comienzo.getDato()
            self.__comienzo = self.__comienzo.getSig()
            self.__cant -= 1

            return d 

    def recorrer(self):

        aux = self.__comienzo

        while aux != None:
            print(aux.getDato())
            aux = aux.getSig()

        print("\n Se recorrio la cola ")
    def getCant(self):
        return self.__cant



