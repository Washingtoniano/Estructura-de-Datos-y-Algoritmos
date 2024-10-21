#Buckets
import numpy as np
class hash():
    __tabla:np.ndarray
    __filas:int
    __columnas:int
    __dimension:int
    __colision:np.ndarray
    __overflow:int
    def __init__(self,claves,buquets):
        self.__filas=int((claves//buquets)+((claves//buquets)*20/100))
        self.__columnas=buquets
        self.__dimension=int(claves//buquets)
        self.__colision=np.zeros(self.__dimension,dtype=int)
        self.__tabla=np.empty(self.__filas,dtype=np)
        self.__overflow=self.__dimension
        for i in range( self.__filas):
            self.__tabla[i]=np.empty(self.__columnas,dtype=object)
    def over(self,clave):
        band=True
        i=self.__overflow
        j=0
        while   j<self.__columnas and i<self.__filas and self.__tabla[i][j]!=None:
            j+=1
            if j==self.__columnas:
                i+=1
                j=0
        if i<self.__filas:
            if self.__tabla[i][j]==None:
                self.__tabla[i][j]=clave
        else:
            band=False
        return band

    def hash(self,clave):
        return int(clave%self.__dimension)
    def insertar(self,clave):
        b=True
        dir=self.hash(clave)
        j=0
        if self.__tabla[dir][j]==None:
            self.__tabla[dir][j]=clave
        else:
            while self.__tabla[dir][j]!=None and self.__colision[dir]<self.__columnas:
                j+=1
            if self.__colision[dir]<self.__columnas:
                self.__tabla[dir][j]=clave
            else:
                b=self.over(clave)
        if b==True:
            self.__colision[dir]+=1
        else:
            print("Overflow lleno")
    def buscar(self,clave):
        p="No se encontro el elemento"        
        dir=self.hash(clave)
        j=0
        while j<self.__columnas and self.__tabla[dir][j]!=clave :
            j+=1
        if j<self.__columnas :
            p=("Se encontro el elemento {} en la fila {} columna {}".format(clave,dir,j))
        
        elif  self.__columnas<=self.__colision[dir]:
                i=self.__overflow
                j=0
                while  i<self.__filas and self.__tabla[i][j]!=clave:
                    j+=1
                    if j==self.__columnas:
                        i+=1
                        j=0
                if i<self.__filas:
                    p=("Se encontro el elemento {} en la posicion {}x{}del overflow".format(clave,i,j)) 
        print(p)

    def mostrar(self):
        for i in range(self.__filas):
            if self.__dimension==i:
                print("Entrando al overflow")
            print(f'[{i}]',end=' ')
            for j in range(self.__columnas):
                print(f'{self.__tabla[i][j]}',end=' ')
            print('\n')