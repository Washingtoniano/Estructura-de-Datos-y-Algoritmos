import numpy as np
class ListSecu():
    __tamaño:int
    __ultimo:int
    __arreglo:np.ndarray
    __cantidad:int
    
    def __init__(self,tamaño=5) -> None:
        self.__tamaño=tamaño
        self.__ultimo=-1
        self.__cantidad=0
        self.__arreglo=np.empty(self.__tamaño,dtype=int)

    def Vacio(self):
        return self.__cantidad==0
    
    def lleno(self):
        return self.__cantidad==self.__tamaño 
       
    def insertar(self,dato,pos):
        if not self.lleno():
            if pos>=0 and pos<=self.__ultimo+1:
                i=self.__ultimo+1
                while i>pos:
                    self.__arreglo[i]=self.__arreglo[i-1]
                    i-=1
                self.__arreglo[i]=dato
                self.__cantidad+=1
                self.__ultimo+=1
                print("El elmento",dato,"fue insertado en la poscion",i)
                
            else:
                print("Posicion no valida")
        else:
            print("Lista llena")
    def Recorrer(self):
        if not self.Vacio():
            i=0
            while i<self.__cantidad:
                print(self.__arreglo[i])
                i+=1
        else:
            print("Lista vacia")
    def Suprimir(self,posicion):
        if not self.Vacio():
            if posicion>=0 and posicion <=self.__ultimo:
                i=self.__ultimo
                eliminado=self.__arreglo[posicion]
                while posicion<i:
                    self.__arreglo[posicion]=self.__arreglo[posicion+1]
                    posicion+=1
                self.__cantidad-=1
                self.__ultimo-=1
            else:
                print("Posicion invalida")  
        else:
            print("Lista vacia")
    def SuprimirPorContenido(self,dato):
        if not self.Vacio():
            i=0
            while i<=self.__ultimo and self.__arreglo[i]!=dato:
                i+=1
                print("Estoy en el while")
            if i<self.__ultimo:
                for j in range(i,self.__ultimo):
                    self.__arreglo[j]=self.__arreglo[j+1]
                print("Se elemino el elemento",dato,"de la posicion",i)
                self.__ultimo-=1
                self.__cantidad-=1
            else:
                print("No se encontro el elemento")


            


    
    def Buscar(self,dato):
        if not self.Vacio():
            i=0
            while dato!=self.__arreglo[i] and i<self.__ultimo:
                i+=1
            if dato==self.__arreglo[i]:
                print("Se encontro el elemento")
                print (self.__arreglo[i])
            else:
                print("No se encontro el elemento")
                print(i)
    def Primero(self):
        if not self.Vacio():
            print("Primero",self.__arreglo[0])
    def Ultimo(self):
        if not self.Vacio():
            print("Ultimo",self.__arreglo[self.__ultimo])
    def Siguiente(self,po):
        if not self.Vacio():
            if po ==self.__ultimo:
                print("En esa posicion esta el ultimo elemento, no tiene siguiente")
            else:

                if po>=0 and po<self.__ultimo:
                    return(self.__arreglo[po+1])
                else:
                    print("Valor invalido")
        else:
            print("Lista vacia")
    def Anterior(self,po):
        if not self.Vacio():
            if po==0:
                print("En esa posicion esta el primer elemento, no tiene anterior")
            else:

                if po>0 and po<=self.__ultimo:
                    return(self.__arreglo[po-1])
                else:
                    print("Valor invalido")
        else:
            print("Lista vacia")
         
    # def InsertarPorContenido(self,dato):
    #     if not self.lleno():
    #         if self.Vacio():
    #             self.__ultimo+=1

    #             self.__arreglo[self.__ultimo]=dato
    #             self.__cantidad+=1
    #         else:
    #             i=0
    #             while i<=self.__ultimo and self.__arreglo[i]<dato:
    #                 i+=1
    #             for j in range(self.__ultimo+1,i-1,-1):
    #                 self.__arreglo[j]=self.__arreglo[j-1]
    #             self.__arreglo[i]=dato
    #             self.__ultimo+=1
    #             self.__cantidad+=1

    def InsertarPorContenido(self,dato):
        if not self.lleno():
            if self.Vacio():
                self.__ultimo+=1
                self.__arreglo[self.__ultimo]=dato
                self.__cantidad+=1
            else:
                if self.__arreglo[self.__ultimo]<dato:
                    self.__ultimo+=1
                    self.__arreglo[self.__ultimo]=dato
                    self.__cantidad+=1
                else:
                    i=self.__ultimo+1
                    while i>0 and self.__arreglo[i-1]>dato:
                        self.__arreglo[i]=self.__arreglo[i-1]
                        i-=1
                    #print(self.__arreglo)
                    #print(self.__arreglo[i-1])
                    #print(self.__arreglo[i])
                    self.__arreglo[i]=dato
                    self.__cantidad+=1
                    self.__ultimo+=1
#Ctrl+k+C
#Ctrl+K+U