import numpy as np
from nodo import nodo
#Encadenada grafo
class grafo():
    __arreglo:np.ndarray
    __vertices:int
    def __init__(self,cant) -> None:
        self.__vertices=cant
        self.__arreglo=np.empty(cant,dtype=nodo)
        for i in range(self.__vertices):
            unnodo=nodo(0)
            self.__arreglo[i]=unnodo
            ori=self.__arreglo[i]
            aux=ori
            for j in range(self.__vertices-1):
                otronodo=nodo(0)
                aux.setSig(otronodo)
                aux=otronodo
    def verificar(self,i):
        return i<=self.__vertices and i>0
    def relacion(self,i,j):
        if self.verificar(i) and self.verificar(j):
            ori=self.__arreglo[i-1]
            aux=ori
            for d in range(j-1):
                aux=aux.getSig()
            aux.setDato(1)
    def mostrar(self):
        for i in range(self.__vertices):
            ori=self.__arreglo[i]
            aux=ori
            print(f'[{i}]',end=' ')
            while aux!=None:
                print(f'{aux.getDato()}',end=' ')
                aux=aux.getSig()
            print("")

