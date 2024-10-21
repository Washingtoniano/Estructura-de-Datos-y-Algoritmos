#Funcion de transformacion: divisiones sucesivas
#Politica de manejo de colisiones:Direccionamiento abierto - secuencia de prueba lineal
#1000 clave

#Direccionamiento abierto
import numpy as np
import random
class hash():
    __arreglo:np.ndarray
    __m:int
    def __init__(self,N=100) -> None:
        self.__m=int(N//0.7)
        self.__arreglo=np.empty(self.__m,dtype=object)
    def hash(self,clave):
        return clave%self.__m
    def insertar(self,clave):
        cont=1
        dir=self.hash(clave)
        while self.__arreglo[dir]!=None and cont !=self.__m:
            cont+=1
            dir=self.hash(dir-1)
        if cont!=self.__m:
            self.__arreglo[dir]=clave
            print( self.__arreglo[dir])
            print ("Comparaciones:",cont)
        else:
            print("Tabla llena")
    def buscar(self,clave):
        print("Buscando")
        dir=self.hash(clave)
        cont=1
        band=False
        while self.__arreglo[dir]!=None and band==False:
            if self.__arreglo[dir]==clave:
                print("El elemento",clave,"se encontro tras",cont,"comparaciones")
                band=True
            else:
                dir=self.hash(dir+1)
                cont+=1
        if band==False:
            print("No se encontro el elemento")
    def mostrar(self):
        for i in range(len(self.__arreglo)):
            print(self.__arreglo[i])
            