import numpy as np

class Pila():
    __tope : int
    __arreglo : np.ndarray
    __cant : int
    __dimension : int

    def __init__(self, dimension=4):
        self.__tope = -1
        self.__cant = 0
        self.__arreglo = np.empty(dimension, dtype = int)
        self.__dimension = dimension
    def lleno(self):
        return self.__dimension==self.__cant

    def insertar(self,dato):

        if self.lleno()==False:
            self.__tope += 1
            self.__arreglo [self.__tope ] = dato
            self.__cant += 1
            #print("En la posicion ",self.__tope,"Inserte",self.__arreglo[self.__tope])
        else: 
            print(" ARREGLO LLENO ")    

    def eliminar(self):
        dato=None
        if self.vacia() == False: 
            dato=self.__arreglo[self.__tope]
            self.__tope -= 1
            self.__cant -= 1

        return dato

    def recorrer(self):
       
        dato = self.__tope
        i=0
        longitud = len(self.__arreglo)

        #for i in range(longitud):
            #print("longitud del arreglo",len(self.__arreglo))
            #print(f"valor tope {self.__tope}")
            #print("Posicion {}".format(dato-i))
            #print(self.__arreglo[dato - i])        

    def vacia(self):
        return(self.__cant == 0)  

