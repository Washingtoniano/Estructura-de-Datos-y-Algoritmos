from nodo import Nodo
import numpy as np
class LC():

    __max:int
    __cab:int
    __cantidad:int
    __nodos:np.empty
    __disponible:int
    def __init__(self,max=5) -> None:
        self.__max=max
        self.__cab=0
        self.__cantidad
        self.__disponible=0
        self.__nodos
        self.__nodos=np.empty(self.__max,dtype=Nodo)
    def Vacio(self):
        return self.__cantidad==0
    def getDisponibilidad(self):#preguntar
        band=False
        i=0
        while i<self.__max and self.__nodos[i].getSiguiente()!=None:
            i+=1
        if i < self.__max:
            self.__disponible=i
            band=True
        else:
            self.__disponible=None
        return band
    def freeDisponible(self,disp):
        if disp>=0 and disp<self.__max:
            self.__nodos[disp].setSiguiente(None)
            print("Exito")
        else:
            print("Fracaso")
    def InsertarPosicion(self,dato,pos):#preguntar
        #if self.__cantidad<self.__max and pos>=0 and pos<=self.__cantidad and self.getDisponibilidad()
        pass
    def InsertarContenido(self,dato):
        #if self.__cantidad<self.__max and 
        pass
    def primero(self):

        if self.Vacio():
            print("Lista vacia")
        else:
            x=self.__nodos[self.__cab].getDato()
            return x
    def Ultimo(self):
        if self.Vacio():
            print("Lista vacia")
        else:
            cabeza=self.__cab
            aux=0
            while cabeza!=-1:#Por que -1
                aux=self.__nodos[cabeza].getDato()
                cabeza=self.__nodos[cabeza].getSiguiente()
            x=aux
            return x
        


