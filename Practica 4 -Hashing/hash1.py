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
        self.__m=int(N//0.7) #el m tiene que ser numero primo
        self.__arreglo=np.empty(self.__m,dtype=object)
    def hash(self,clave):
        return clave%self.__m
    def insertar(self,clave):
        cont=1
        dir=self.hash(clave)
        while self.__arreglo[dir]!=None and cont !=self.__m:
            cont+=1
            dir=(dir+1)%self.__m
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
                dir=(dir+1)%self.__m
                cont+=1
        if band==False:
            print("No se encontro el elemento")
    def mostrar(self):
        for i in range(len(self.__arreglo)):
            print(self.__arreglo[i])

    def conversion(self,clave):
        n=0
        clave=str(clave)
        lon=len(clave)
        for i in range(lon):
            n+=clave[i]
        return n
    
    
    def primo(self,clave):
        i=1
        con=1
        print("Clave",clave)
        for i in range(2,10):
            r=clave%i
            if r==0 and i!=clave:
                con+=1
        print("r:",r)
        if con!= 1:
            band=False
            prim=self.conversion(clave)
            print("prim:",prim)
            while band==False:
                con=1
                prim+=1
                print("prim:",prim)

                for i in range(2,10):
                    r=prim%i
                    if r==0 and i!=clave:
                        con+=1
                print("prim:",prim)
                print("r:",r)

                if con==1:
                    band=True
            



