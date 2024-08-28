import numpy as np

class ColaSecu():
    __arreglo : np.ndarray
    __cantidad : int
    __dimension : int
    __ultimo : int
    __primero : int

    def __init__(self,dimension = 4):
        self.__arreglo = np.empty(dimension, dtype = int)
        self.__cantidad = 0
        self.__ultimo = 0
        self.__dimension = dimension
        self.__primero = 0    

    def vacio(self):
        return self.__cantidad == 0  

    def insertar(self,dato):

        if (self.__dimension > self.__cantidad):
            self.__arreglo[self.__ultimo] = dato
            self.__ultimo = (self.__ultimo + 1) % self.__dimension 
            self.__cantidad += 1
        else:
            print("\n COLA LLENA")
    
    def suprimir(self):

        x = None

        if self.vacio() == True:
           print("\n COLA VACIA")

        else:
            x = self.__arreglo[self.__primero]
            self.__cantidad =self.__cantidad - 1
            self.__primero=(self.__primero+1)%self.__dimension
            return x 

    def recorrer(self):

        if self.vacio() != True:
            i = self.__primero
     
            for j in range(self.__cantidad):
                print(self.__arreglo[i])
                i = (i+1) % self.__dimension    
    def getCant(self):
        return self.__cantidad       
        




    