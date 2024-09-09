import numpy as np
class ListaSec():
    __arreglo:np.ndarray
    __primero:None
    __ultimo:None
    __dimension:int
    __cant:int
    def __init__(self,dimension=5) -> None:
        self.__dimension=dimension
        self.__arreglo=np.empty(self.__dimension,dtype=int)
        self.__primero=None
        self.__ultimo=None
        self.__cant=0
    def Insertar(self,dato):
        if self.__cant==0:
            self.__primero=dato
        elif self.__cant==self.__dimension-1:
            self.__ultimo=dato
        self.__arreglo[self.__cant]=dato
        self.__cant+=1
    def vacio(self):
        return self.__cant==0
    def Primero(self):
        return self.__primero
    def Ultimo(self):
        return self.__ultimo
    def Recorrer(self):
        if self.vacio()!=True:
            for i in range ((self.__cant)):
                print(self.__arreglo[i])
        else:
            print("Lista Vacia")
    def Siguiente(self,p):
        if p>=self.__dimension-1:
            print ("Lista fuera de rango")
        else:
            return self.__arreglo[p+1]
    def Anterior(self,p):
        if p<=0:
            print("Lista fuera de rango")
        else:
            return self.__arreglo[p-1]
    def Suprimir(self,p):
        if self.vacio()==True:
            print("Lista vacia")
        else:
            if p<self.__cant:
                
                while p< self.__dimension and self.Siguiente(p)!=None:
                    self.__arreglo[p]=self.Siguiente(p)
                    p+=1
                if self.Siguiente(p)==None:
                    self.__arreglo[p]=0
            x=self.__arreglo[p]
            self.__cant-=1

            return x
    def recuperar(self,p):
        return self.__arreglo[p]
    def buscar(self,x):
        d=0
        i=0
        while self.recuperar(i)!=x and i <self.__cant:
            i+=1
        if self.recuperar(i)==x:
            d=self.recuperar(i)
        return d
    def elimarDUp(self):
        i=0
        j=0
        for i in range ((self.__cant)):

            for j in range((self.__cant)):
                if j!=i:
                    if self.__arreglo[j]==self.__arreglo[i]:
                        self.Suprimir(j)
        