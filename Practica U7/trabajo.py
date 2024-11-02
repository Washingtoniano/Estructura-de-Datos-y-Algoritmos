import numpy as np
from Lista_Arbol import Lista_enca
from caracter import caracter
from ListaEncaOrd import lista
class trabajo():
    __arreglo:np.ndarray
    __cant:int
    def __init__(self,cant=8):
        self.__cant=cant
        self.__arreglo=np.empty(self.__cant,dtype=object)
    def MCodigo(self):
        Codigos=self.__arreglo[1]
        Codigos.mostrar()
    def comprobacion(self,cad):
        band=True
        j=0
        while j<len(cad) and band==True:
            if cad[j]!='0' and cad[j]!='1':
                band=False
            j+=1
        return band
    def Mayuscula(self):
        if self.__arreglo[2]==None:
            cad=self.__arreglo[0]
            self.__arreglo[2]=cad.upper()
        else:
            print(self.__arreglo[2])
    def Minuscula(self):
        if self.__arreglo[3]==None:
            cad=self.__arreglo[0]

            self.__arreglo[3]=cad.lower()
        else:
            print(self.__arreglo[3])
    def eliminacion(self,cad):
        #4
        pass
    def seHizo(self,cad,i):
        band=False
        if self.__arreglo[5]!=None:
            if len(cad) == len(self.__arreglo[5]) :
                if i<len(cad):
                    if self.__arreglo[5][i]==cad[i]:
                        band=self.seHizo(cad,i+1)
                else:
                    band=True
        return band




    def deco(self,cad):
        #if self.__arreglo[2]!=None and self.__arreglo[2]==cad:
        #    print("Codigo ya ingresado, decodificacion",)
        if self.comprobacion(cad):
            if self.seHizo(cad,0)==True:
                print("La operacion ya se realizo, los resultados fueron:")
                print("Para la secuencia {} el codigo es{}".format(self.__arreglo[5],self.__arreglo[6]))

            else:
                l=[]
                primero=self.__arreglo[1].getPrimero()
                m=len(self.__arreglo[1].getPrimero().getCodigo())
                long=len(cad)
                i=0
                aux=primero
                while i<long and aux!=None:
                    m=len(aux.getCodigo())
                    pri=str(aux.getCodigo())

                    ne=cad[i]
                    for j in range(i+1,m):
                        ne+=cad[j]
                        pri+=str(aux.getCodigo()[j])
                    if pri==ne:
                        l.append(aux.getDato())
                        i+=m
                    aux=aux.getSiguiente()
                    if aux==None:
                        aux=primero
                print("Codigo")
                p=str(l)
                
                print(p)
                self.__arreglo[5]=cad
                self.__arreglo[6]=l
        else:
            print("No se pudo decoficar")


            
    def inicializar(self,cadena):
        self.__arreglo[0]=cadena
        self.Mayuscula()
        self.Minuscula()
        lis=Lista_enca()
        
        ora=cadena.upper()
        self.generacion(ora,lis)
        raiz=lis.Primero()
        long=len(raiz.getDato())
        lon=len(cadena)
        for i in range((long)):
            uncaracter=self.frecuencia(lon,ora,raiz.getDato()[i])
            lis.Codigos(raiz,uncaracter)
        l=lista()
        lis.hojas(raiz,l)
        self.__arreglo[1]=l          

    def frecuencia(self,long,ora,d):
        uncaracter=caracter(d)
        cont=0
        for i in range (long):
            if d==ora[i]:
                cont+=1
        uncaracter.setFrecuencia(cont)       
        return uncaracter
            
    def generacion(self,ora,lis):
        long=len(ora)
        for i in range(long):
            
            uncaracter=self.frecuencia(long,ora,ora[i])
       
            
            if lis.Buscar(uncaracter)==False or lis.Vacio()==True:
  
                lis.insertar(uncaracter)
        while lis.Uno()==False:
            primero=lis.Suprimir(lis.Primero())
            segundo=lis.Suprimir(lis.Primero())
            #print(primero.getCaracter())
            #print(segundo.getCaracter())

            nuevo=caracter(primero.getDato()+segundo.getDato())
            nuevo.setIzquierda(primero)
            nuevo.setDerecha(segundo)
          
            fre=primero.getFrecuencia()+segundo.getFrecuencia()


            nuevo.setFrecuencia(fre)
            lis.insertar(nuevo)
