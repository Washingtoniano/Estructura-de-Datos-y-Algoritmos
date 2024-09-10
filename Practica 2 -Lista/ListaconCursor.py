from nodo import Nodo
import numpy as np
class LC():

    __max:int
    __cab:int
    __cantidad:int
    __nodos:np.ndarray
    __disponible:int

    def __init__(self,max=5) -> None:
        self.__max=max
        self.__cab=0
        self.__cantidad=0
        self.__disponible=0
        
        self.__nodos=np.empty(self.__max,dtype=Nodo)

    def Vacio(self):
        return self.__cantidad==0
    def getDisponibilidad(self):#preguntar
        band=False
        i=0
        while i<self.__max and self.__nodos[i].getSiguiente()!=None:
            i+=1
        if i < self.__max:
            self.__disponible=i
            band=True
        else:
            self.__disponible=None
        return band
    def freeDisponible(self,disp):
        if disp>=0 and disp<self.__max:
            self.__nodos[disp].setSiguiente(None)
            print("Exito")
        else:
            print("Fracaso")
    def InsertarPosicion(self,dato,pos):#preguntar
        if self.__cantidad<self.__max and pos>=0 and pos<=self.__cantidad and self.getDisponibilidad():
            self.__nodos[self.__disponible].setDato(dato)
            ant=self.__cab
            cabeza=self.__cab
            i=0
            while i<pos:
                i+=1
                ant=cabeza
                cabeza =self.__nodos[cabeza].getSiguiente()

            if cabeza==self.__cab:      #Inserta al Inicio
                if self.Vacio():
                    self.__nodos[self.__cab].setSiguiente(None)

                else:                   #Inserta en la lista
                    self.__nodos[self.__disponible].setSiguiente(self.__cab)
                self.__cab=self.__disponible

            elif cabeza==None: #Inserta al final
                self.__nodos[self.__disponible].setSiguiente(cabeza)
                self.__nodos[ant].setSiguiente(self.__disponible)
            self.__cantidad+=1
        else:
            print("Espacio lleno")
                
     

    def InsertarContenido(self,dato):
        if self.__cantidad<self.__max and self.getDisponibilidad():
            ant=self.__cab 
            cabeza=self.__cab
            i=0
            while i <self.__cantidad and cabeza!=None and self.__nodos[cabeza].getDato()<dato:
                i+=1
                ant=cabeza
                cabeza=self.__nodos[cabeza].getSiguiente()
            if cabeza ==self.__cab:   #Inserta al inicio
                if self.Vacio():
                    self.__nodos[self.__cab].setSiguiente(None) #Lista vacia
                else:
                    self.__nodos[self.__disponible].setSiguiente(self.__cab) #Inserta en la lista
                self.__cab=self.__disponible
            elif cabeza==None:
                self.__nodos[self.__disponible].setSiguiente(None)
                self.__nodos[ant].setSiguiente(self.__disponible)
            else:
                self.__nodos[self.__disponible].setSiguiente(cabeza)
                self.__nodos[ant].setSiguiente(self.__disponible)
            self.__cantidad+=1
        else:
            print("Espacio lleno")


    def Suprimir(self,pos):
        if not self.Vacio():
            if self.__cantidad>pos and pos<=0:
                ant =self.__cab
                cabeza=self.__cab
                i=0
                while i<pos and cabeza !=None:
                    i+=1
                    ant=cabeza
                    cabeza =self.__nodos[cabeza].getSiguiente()
                if cabeza ==self.__cab:
                    if self.__cantidad==1:
                        self.__cab=0
                    else:
                        self.__cab=self.__nodos[ant].setSiguiente()
                else:
                    self.__nodos[ant].setSiguiente(self.__nodos[cabeza].getSiguiente())
                    x=self.__nodos[cabeza].getDato()
                    self.__disponible=cabeza
                    self.freeDisponible(self.__disponible)
                    self.__cantidad-=1
            else:
                print("Posicion incorrecta")
        else:
            print("Lista vacia")
    def SuprimirPorContenido(self,dato):
        pass

    def recuperar(self,pos):
        if not self.Vacio():
            if 0<=pos and self.__cantidad>pos:
                cabeza=self.__cab
                i=0
                while cabeza !=None and i<pos:
                    i+=1
                    cabeza=self.__nodos[cabeza].getSiguiente()
                x=self.__nodos[cabeza].getdato()
                return x
            else:
                print("Posicion invalida")
        else:
            print("Lista vacia")
    def Buscar(self,dato):
        if not self.Vacio():
            cabeza=self.__cab
            i=0
            while cabeza!=None and i< self.__cantidad and self.__nodos[cabeza].getDato()!=dato:
                i+=1
                cabeza =self.__nodos[cabeza].getSiguiente()
            if i<self.__cantidad:
                print("El elmento buscado esta en la posicion",i)
            else:
                print("No se encontro el elemento")

        else:
            print("Lista vacia")
    def primero(self):

        if self.Vacio():
            print("Lista vacia")
        else:
            x=self.__nodos[self.__cab].getDato()
            return x
    def Ultimo(self):
        if self.Vacio():
            print("Lista vacia")
        else:
            cabeza=self.__cab
            aux=0
            while cabeza!=-1:#Por que -1
                aux=self.__nodos[cabeza].getDato()
                cabeza=self.__nodos[cabeza].getSiguiente()
            x=aux
            return x
    def Siguiente(self,pos):
        if not self.Vacio():
            if self.__cantidad>pos and 0<=pos:
                if pos==self.__cantidad-1:
                    print("El ultimo elemento no tiene siguiente")
                else:
                    cab=self.__cab
                    i=0                    
                    while i<self.__cantidad and i!=pos:
                        cab=self.__nodos[cab].getSiguiente()
                        i+=1
                    cab=self.__nodos[cab].getSiguiente()
                    print("Siguiente",cab.getDato()) 
            else:
                print("Posicion no valida")
        else:
            print("Lista vacia")
    def anterior(self,pos):
        if not self.Vacio():
            if self.__cantidad>pos and 0<=pos:
                if pos==0:
                    print("El primer elemento no tiene anterior")
                else:
                    i=0
                    cab=self.__cab
                    ant=cab
                    while i<self.__cantidad and i!=pos:
                        ant=cab
                        cab=self.__nodos[cab].getSiguiente()
                        i+=1
                    print("Siguiente",self.__nodos[ant].getDato()) 
            else:
                print("Posicion no valida")
        else:
            print("Lista vacia")
    def recorrer(self):
        if not self.Vacio():
            cabeza=self.__cab
            print("Lita")
            while cabeza!=None:
                print(self.__nodos[cabeza].getDato())
                cabeza=self.__nodos[cabeza].getSiguiente()
        else:
            print("Lista vacia")
        


