import numpy as np
from lista import lista

from nodo import nodo
#Secuecial
#Adyacencia
#conexo
#grafo
#Agregar todos los metodos, no importa si son para grafo, digrafo, conexo, no conexo, ciclico, aciclico,etc
#Opcion: agregar banderas para saber que tipo de grafo estamos trabajando o crear un metodo para comprobarlo
class grafo():
    __vertices:int
    __matriz:np.ndarray
    __dirigido:bool
    def __init__(self,ver,d=False) -> None:
        self.__vertices=ver
        self.__matriz=np.empty(ver,dtype=object)
        for i in range(self.__vertices):
            self.__matriz[i]=np.zeros(ver,dtype=int)
        self.__dirigido=d
    def relacion(self,i,j):
        if self.verificar(i) and self.verificar(j):
            self.__matriz[i-1][j-1]=1
            if self.__dirigido==False:
                self.__matriz[j-1][i-1]=1
    def pesos(self,i,j,cant):
        if self.verificar(i) and self.verificar(j):
            self.__matriz[i-1][j-1]=cant
            self.__matriz[j-1][i-1]=cant
 

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
    def comprobar(self,i,j,l):
        band=0
        d=0
        lon=l.getcant()
        while d<lon and band ==False:
            if l[d]==j+1:
                band=d
            d+=1
        return band
                
    def recursiva2(self,i,j,l,p):
        if i< self.__vertices:
            d=self.comprobar(i,j,l)
            if d!=False:
                j+=d
            if j<self.__vertices:
                if self.__matriz[i][p]==1:
                    l.append(p+1)
                    band=True

                else:
                    if self.__matriz[i][j]!=1:
                        j+=1
                        band=self.recursiva2(i,j,l,p)
                    else:
                        #Problema
                        l.append(j+1)
                        band=self.recursiva2(j,0,l,p)
            else:
                band=False   
            if band==False:
                l.remove(i+1)         
        return band
    

    

    #i movimiento en filas- j movimiento en columnas - l lista creada por el programador -p posicion del elemento a buscar o fila anterior al salto(evita ciclo)
    #Nota (Solucionar): existe la posibilidad que se produsca un ciclo si hay mas de un salto, por ejemplo 1-2-3-5-2 el primero evita e¿la vuelta a 1 el o la vuelta a 3 pero no hay forma de evitar la vuelta a 2. 
    def recursiva(self,i,j,l,p,o):
        if i< self.__vertices:
            if l.primero()-1==j:#evita que vuelva al primero
                j+=1
            if j==o: #evita que vuelva al anterior
                j+=1
            if i ==j: #evita ciclo
                j+=1


            if j<self.__vertices:
                if self.__matriz[i][p]==1: ##Comprueba posicin
                    band=True

                else:

                    if self.__matriz[i][j]!=1: #Se mueve por las columnas
                        j+=1
                        band=self.recursiva(i,j,l,p,o)
                    else:
                        b=i
                        h=j+1
                        l.insertar(h)
                        band=self.recursiva(j,0,l,p,b) #se mueve por las filas
                        if band==False:
                            l.eliminar()
            else:
                band=False  
        
        return band
    
    # hacerlo iterativo usar los metodos en la teoria (BEP,BEA)
    def camino(self,u,v):
        if self.verificar(u) and self.verificar(v):
            unalista=lista()
            b=False
            i=u-1
            j=v-1
            unalista.insertar(u)
            if self.__matriz[i][j]==1:
                b=True
                unalista.insertar(v)
            else:
                d=0
                while d<self.__vertices and b==False:
                    if i!=d:
                        #unalista.insertar(d+1)
                        b=self.recursiva(i,d,unalista,j,i)
                    #b=self.recursiva2(d,0,l,j)
                    if b==False:
                        unalista.eliminar()
         
                    d+=1
                if b==True:
                    ulti= unalista.getUltimo()
                    if self.__matriz[ulti-1][i]==1:
                        unalista.reset()
                        unalista.insertar(u)
                        unalista.insertar(ulti)
                    unalista.insertar(v)
                    unalista.mostrar()
                else:
                    print("No hay camino")
                unalista.reset()
            return b

    def grado(self,n):
        if self.verificar(n):
            cont=0
            i=n-1
            for j in range(self.__vertices):
                if self.__vertices[i][j]==1:
                    cont+=1
            print("Grado del nodo",n,cont)
    
    
    
    def conexo(self):
        i=0
        band=True
        while i in range(self.__vertices) and band==True:
            j=0
            while j in range(self.__vertices) and band==True: 
                if i!=j:
                    if self.__matriz[i][j]==0 or self.__matriz[j][i]==0:
                        band=False
                j+=1
            i+=1
        return band
    
    def aciclico(self): #No funciona
        i=0
        band=False
        while i <self.__vertices and band==False:
            band=self.camino(i+1,i+1)
            i+=1
        if band ==False:
            print("El grafo no presenta ciclos")
        else:
            print("EL grafo presenta ciclos")
         
    def BEA(self,o):
        arreglo=np.ndarray(self.__vertices,dtype=object)
        for i in range (self.__vertices):
            arreglo[i]=None
        arreglo[o-1]=0
        from ColaSecuencial import ColaSecu
        cola=ColaSecu(self.__vertices)
        cola.insertar(o)
        while cola.vacio()==False:
            a=cola.suprimir()-1
            for i in range (self.__vertices):
                if self.__matriz[a][i]==1:
                    if arreglo[i]==None:
                        arreglo[i]=arreglo[a]+1
                        cola.insertar(arreglo[i]+1)
        print("Busqueda BEA")
        for i in range(self.__vertices):
            print(f'[{i+1}]',end=' ')
            print(f'{arreglo[i]}',end=' ')
            print('')
    def visita(self,u,tiempo,ar,ar2):
        tiempo=tiempo+1
        ar[u]=tiempo
        for i in range(self.__vertices):
            if self.__matriz[u][i]==1:
                if ar[i]==0:
                    self.visita(i,tiempo,ar,ar2)
        tiempo=tiempo+1
        ar2[u]=tiempo
        print("Tiempo total en visita:",tiempo)
        #2 arreglos - ida y vuelta- problema con nodo fuente

    def BEP(self):
        arreglo=np.ndarray(self.__vertices,dtype=object)
        arreglo2=np.ndarray(self.__vertices,dtype=object)
        for i in range(self.__vertices):
            arreglo[i]=0
            arreglo2[i]=0
        tiempo =0
        for i in range(self.__vertices):
            if arreglo[i]==0:
                self.visita(i,tiempo,arreglo,arreglo2)
        print("Los nodo presentan un tiempo de:")
        for i in range(self.__vertices):
            print("Nodo {}, Tiempo de ida: {} Tiempo de vuelta: {} \n".format(i+1,arreglo[i],arreglo2[i]) )
        print("Tiempo total:",tiempo)

#DIGRAFO
    def CantEntradas(self,i):
        if self.verificar(i):
            cont=0
            d=i-1
            for j in range(self.__vertices):
                if self.__matriz[j][d]==1:
                    cont+=1
            return cont
    def CantSalidas(self,i):
        if self.verificar(i):
            cont=0
            d=i-1
            for j in range(self.__vertices):
                if self.__matriz[d][j]==1:
                    cont+=1
            return cont
    def Fuente(self,i):
        if self.verificar(i):
            band=False
            s=self.CantSalidas(i)
            e=self.CantEntradas(i)
            if e==0 and s!=0:
                band=True
            return band
    def Sumidero(self,i):
        if self.verificar(i):
            band=False
            s=self.CantSalidas(i)
            e=self.CantEntradas(i)
            if e!=0 and s==0:
                band=True
            return band





