import numpy as np
from Lista_Arbol import Lista_enca #Generacion de arbolS
from caracter import caracter #Nodo Cadena
from ListaEncaOrd import lista #Obtencion de hojas del arbol(Letras y codigos)
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
    def seHizo(self,cad,aux):
        band=False
        if aux!=None:
            cod=aux.getCodigo()
            if len(cad) == len(cod) :
                band=True
  
                i=0
                while i <len(cad) and band==True:
                    if cod[i]!=cad[i]:
                        band=False
                    i+=1
                if band==False:
                    band=self.seHizo(cad,aux.getSiguiente())
                else:
                    band=aux
        return band


    def Decifrado(self,aux,cad):
        if aux.getSiguiente()!=None:
            self.Decifrado(aux.getSiguiente(),cad)
        else:
            aux.setSiguiente(cad)

    def deco(self,cad):
        #if self.__arreglo[2]!=None and self.__arreglo[2]==cad:
        #    print("Codigo ya ingresado, decodificacion",)
        if self.comprobacion(cad):
            auxi=self.__arreglo[5]
            dato=self.seHizo(cad,auxi)
            if dato!=False:
                print("La operacion ya se realizo, los resultados fueron:")
                print("Para la secuencia {} el codigo es {}".format(dato.getCodigo(),dato.getDato()))

            else:
                l=None
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
                        if l==None:
                            l=aux.getDato()
                        else:
                            l+=aux.getDato()
                        i+=m
                    aux=aux.getSiguiente()
                    if aux==None:
                        aux=primero
                print("Codigo")
                p=str(l)
                
                print(p)
                #Probar usar los nodos cadenas y generar una lista de nodos con mayor cantidad de datos y menos espacio del arreglo
                cadena=caracter(l)
                cadena.setCodigo(cad)
                if self.__arreglo[5]==None:

                    self.__arreglo[5]=cadena
                else:
                    self.Decifrado(auxi,cadena)

                #Comprobar si se puede mostrar el formato mas bonito
        else:
            print("No se pudo decoficar")


            
    def inicializar(self,cadena):
        for i in range(self.__cant):
            self.__arreglo[i]=None
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
