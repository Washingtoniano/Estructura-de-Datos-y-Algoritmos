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
        self.__m=int(self.primo(N)//0.7) #el m tiene que ser numero primo
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

    def comprobacion(self,clave):
        band=False
        con=1
        print("Clave",clave)
        i=2
        while i<clave and con==1:
            r=clave%i
            if r==0 and i!=clave:
                con+=1
            i+=1
        if con==1:
            band=True
        #print("r:",r)
            
        return band
    
    
    def primo(self,clave):
        r=clave
        if not self.comprobacion(clave):
            #n=0
            #clave=str(clave)
            #lon=len(clave)
            #for i in range(lon):
            #    n+=int(clave[i])
            band=False
            print("prim:",r)
            while band==False:
                r+=1
                print("prim:",r)
                if(self.comprobacion(r)):
                    band=True
                    #r=n
                #else:
                #    n+=1
        return r



