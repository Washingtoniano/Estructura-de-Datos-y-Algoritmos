import numpy as np
from nodo import nodo
#Secuecial
#Adyacencia
#conexo
#grafo
class grafo():
    __vertices:int
    __matriz:np.ndarray
    def __init__(self,ver) -> None:
        self.__vertices=ver
        self.__matriz=np.empty(ver,dtype=object)
        for i in range(self.__vertices):
            self.__matriz[i]=np.zeros(ver,dtype=int)
    def relacion(self,i,j):
        if self.verificar(i) and self.verificar(j):
            self.__matriz[i-1][j-1]=1
            self.__matriz[j-1][i-1]=1
    def verificar(self,i):
        return i<=self.__vertices and i>0
    def mostrar(self):
        print("Matriz de adyacencia de un grafo")
        for i in range((self.__vertices)):
            d=i+1
            print(f'[{d}]',end=' ')
            for j in range(self.__vertices):
                print(f'{self.__matriz[i][j]}',end=' ')
            print("")
    def adyacentes(self,N):
        if self.verificar(N):
            l=[]
            for i in range(self.__vertices):
                if self.__matriz[N-1][i]==1:
                    l.append(i+1)
            lon=len(l)
            if lon!=0:
                print("El vertice",N,"es adyacente con:")
                for j in range(lon):
                    print(l[j],end='')
                print("")

    def camino(self,u,v):
        if self.verificar(u) and self.verificar(v):
            l=[]
            b=False
            i=u-1
            j=v-1
            l.append (u)
            if self.__matriz[i][j]==1:
                b=True
                l.append(v)
            else:
                d=0
                while d<self.__vertices and b==False:
                    if self.__matriz[i][d]==1:
                        if self.__matriz[d][j]==1:
 
                            b=True
                    d+=1
                if b==True:
                    l.append(d+1)
                    l.append(v)
            return b

    def grado(self,n):
        if self.verificar(n):
            cont=0
            i=n-1
            for j in range(self.__vertices):
                if self.__vertices[i][j]==1:
                    cont+=1
            print("Grado del nodo",n,cont)