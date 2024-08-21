import numpy as np
class ColaSecu():
    __arreglo:np.ndarray
    __cant:int
    __dimension:int
    __primero:int
    __ultimo:int

    def __init__(self,dimension=4) -> None:
        self.__arreglo=np.empty(dimension,dtype=int)
        self.__dimension=dimension
        self.__cant=0
        self.__primero=0
        self.__ultimo=dimension-1
    def lleno(self):
        return self.__dimension==self.__cant
    def vacio(self):
        return self.__cant==0

    def agregar(self,dato):
        if self.lleno()==False:

            self.__arreglo[self.__cant]=dato
            self.__cant+=1
        else:
            print("Arreglo lleno")
    def elimnar(self):
        d=None
        if self.vacio()==False:
            self.__cant-=1
            x=self.__arreglo[self.__primero]
            self.__primero+=1
            d=x
        return d
    def recorrer(self):
        for i in range (len(self.__arreglo)):
            print(self.__arreglo[i])

