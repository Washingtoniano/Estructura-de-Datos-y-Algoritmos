import numpy as np
from nodo import nodo
class hash():
    __arreglo:np.ndarray
    __col:int
    __dim:int
    __cant:int
    def __init__(self,colision,cla=1000) -> None:
        self.__cant=cla
        self.__col=colision
        self.__dim=cla//self.__col
        self.__arreglo=np.empty((self.__dim),dtype=nodo)

    def hash(self,clave):
        return int(clave%(self.__dim))
    def mostrar(self):
        for i in range ((self.__dim)):
            dato=self.__arreglo[i]
            if dato!=None:
                dato.mostrar()
            else:
                print(dato)
             

    def buscar(self,clave):
        encontrado=None
        pos=self.hash(clave)
        dato=self.__arreglo[pos]
        if dato!=None:
                
            if clave==dato.getDato():
                encontrado=clave
            else:
                encontrado=dato.Buscar(clave)
            if encontrado==None:
                print("No se encontro el dato")
            else:
                print("El dato", encontrado,"esta en el arreglo(posicion",pos,")")
        else:
            print("Posicion vacia")

    def insertar(self,clave):
        #if self.espacio()==True:
            unnodo=nodo(clave)
            dire=self.hash(clave)
            #dire=self.hash(dire)
            if self.__arreglo[dire]==None:
                self.__arreglo[dire]=unnodo
                print(self.__arreglo[dire])
                print("Clave:",unnodo.getDato())
            else:
                ori=self.__arreglo[dire]
                ori.insertar(unnodo)

                print(self.__arreglo[dire])
                print("Clave:",unnodo.getDato())

