import numpy as np
from nodo import nodo
#Encadenada grafo
class grafo():
    __arreglo:np.ndarray
    __vertices:int
    __band:bool
    def __init__(self,cant,d=False) -> None:
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
        self.__band=d
    def verificar(self,i):
        return i<=self.__vertices and i>0
    def relacion(self,i,j):
        if self.verificar(i) and self.verificar(j):
            ori=self.__arreglo[i-1]
            aux=ori
            if self.__band==False:
                for d in range(j-1):
                    aux=aux.getSig()
                aux.setDato(1)
            else:
                otro=self.__arreglo[j-1]
                auxi=otro
                for d in range(j-1):
                    aux=aux.getSig()
                    
                aux.setDato(1)
    
                for h in range(i-1):
                    auxi=auxi.getSig()
                auxi.setDato(1)
                    
                        
                    
    def mostrar(self):
        for i in range(self.__vertices):
            ori=self.__arreglo[i]
            aux=ori
            print(f'[{i+1}]',end=' ')
            while aux!=None:
                print(f'{aux.getDato()}',end=' ')
                aux=aux.getSig()
            print("")
    def adyacentes(self,i):
        if self.verificar(i):
            ori=self.__arreglo[i-1]
            aux=ori
            if aux!=None:
                j=1
                print("Adyacentes de",i)
                while aux!=None:
                    if aux.getDato()==1:
                        print(j,end=' ')
                    aux=aux.getSig()
                    j+=1
                print(" ")
            else:
                print("No tiene adyacentes")
    
    #Digrafo
    def CantEntradas(self,i):
        Cont=0
        if  self.verificar(i):
            n=i-1
            for j in range(self.__vertices):
                d=0
                otro=self.__arreglo[j]
                aux=otro
                while otro!=None and d!=n:
                    aux=aux.getSig()
                    d+=1
                if aux!=None:
                    if aux.getDato()==1:
                        Cont+=1
        return Cont
    def CantSalidas(self,i):
        Cont=0
        if  self.verificar(i):
            n=i-1
            ori=self.__arreglo[n]
            aux=ori
            while aux!=None:
                if aux.getDato()==1:
                    Cont+=1
                aux=aux.getSig()
        return Cont
                        
    def Fuente(self,i):
        if self.verificar(i):
            b=False
            if self.CantEntradas(i)==0 and self.CantSalidas(i)!=0:
                b=True
            return b
    def Sumidero(self,i):
        if self.verificar(i):
            b=False
            if self.CantEntradas(i)!=0 and self.CantSalidas(i)==0:
                b=True
            return b
        #wireshark Adyacente
        #distrack ponderado