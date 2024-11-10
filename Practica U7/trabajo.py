import numpy as np
from Lista_Arbol import Lista_enca #Generacion de arbolS
from caracter import caracter #Nodo Cadena
from ListaEncaOrd import lista #Obtencion de hojas del arbol(Letras y codigos)

#0 _Cadena original
#1 -Raices del Codigo de Huffman
#2 -Mayuscula
#3 -Minuscula
#4 -Cambio de cadenas
#5 - Registro de cadenas encontradas
#6 -Codig de cadena actual
class trabajo():
    __arreglo:np.ndarray
    __cant:int
    def __init__(self,cant=8):
        self.__cant=cant
        self.__arreglo=np.empty(self.__cant,dtype=object)
    def transformacion(self,cadena):
        CadOri=self.__arreglo[0]
        m=len(CadOri)
        n=len(cadena)

        arreglo=np.zeros(m+1,dtype=object)
        for i in range(m+1):
            arreglo[i]=np.zeros(n+1,dtype=int)
        for i in range(m+1):
            arreglo[i][0]=i
        for j in range(n+1):
            arreglo[0][j]=j
        for i in range(1,m+1):
            for j in range(1,n+1):
                if CadOri[i-1]==cadena[j-1]:
                    arreglo[i][j]=arreglo[i-1][j-1]
                else:
                    arreglo[i][j]=min(arreglo[i][j-1],arreglo[i-1][j],arreglo[i-1][j-1])+1
        for i in range(m+1):
            print(f'[{i}]', end=' ')
            for j in range(n+1):
                print(arreglo[i][j],end=' ')
            print("")
        #Se genera un mtriz en la que cada elemento nos muestra el tiempo necesario para transformar una cadena a otra, segun la subcadena en la que estemos       

        self.inicializar(cadena)
    def MCodigo(self):
        Codigos=self.__arreglo[1]
        Codigos.mostrar()
    def comprobacionR(self,cad,j=0):
        band=True
        if j<len(cad):
            if cad[j]!='0' and cad[j]!='1':
                band=False
            else:
                j+=1
                band=self.comprobacionR(cad,j)
        return band
    # def comprobacion(self,cad):
    #     band=True
    #     j=0
    #     while j<len(cad) and band==True:
    #         if cad[j]!='0' and cad[j]!='1':
    #             band=False
    #         j+=1
    #     return band
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
    def decor2(self,h,m,long,ne,cad):
        if h<m and h<long:
            if ne==None:
                ne=cad[h]
            else:
                ne+=cad[h]
            h+=1
            ne=self.decor2(h,m,long,ne,cad)
        return ne
    def decor1(self,i,long,aux,cad,l,primero):
        if i<long:
            m=len(aux.getCodigo())
            pri=str(aux.getCodigo())
            ne=None
            h=i
            m=m+h
            ne=self.decor2(h,m,long,ne,cad)
            if pri==ne:
                if l==None:
                    l=aux.getDato()
                else:
                    l+=aux.getDato()
                i=m
            aux=aux.getSiguiente()
            if aux==None:
                    aux=primero
            l=self.decor1(i,long,aux,cad,l,primero)
        return l

    def deco(self,cad):
        #if self.__arreglo[2]!=None and self.__arreglo[2]==cad:
        #    print("Codigo ya ingresado, decodificacion",)
        if self.comprobacionR(cad):
            if cad==self.__arreglo[6]:
                print("La secuencia ingresada pertenece a la cadena de origen",self.__arreglo[0])
            else:
                auxi=self.__arreglo[5]
                dato=self.seHizo(cad,auxi)
                if  dato!=False:
                    print("La operacion ya se realizo, los resultados fueron:")
                    print("Para la secuencia {} el codigo es {}".format(dato.getCodigo(),dato.getDato()))

                else:
                    l=None
                    primero=self.__arreglo[1].getPrimero()
                    long=len(cad)
                    i=0
                    aux=primero
                    l=self.decor1(i,long,aux,cad,l,primero)
                    # while i<long and aux!=None:
                    #     m=len(aux.getCodigo())
                    #     pri=str(aux.getCodigo())
                    #     ne=None
                    #     h=i
                    #     m=m+h
                    #     # while h<m and h<long:
                    #     #     if ne==None:
                    #     #         ne=cad[h]
                    #     #     else:
                    #     #         ne+=cad[h]
                    #     #     h+=1
                    #     #     #pri+=str(aux.getCodigo()[j])
                    #     ne=self.decor(h,m,long,ne,cad)
                    #     if pri==ne:
                    #         if l==None:
                    #             l=aux.getDato()
                    #         else:
                    #             l+=aux.getDato()
                    #         i=m
                    #     aux=aux.getSiguiente()
                    #     if aux==None:
                    #         aux=primero
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
                        #No es necesario guardar todas la cadenas,
        else:
            print("No se pudo decoficar")


    def codigo(self,dato,c,cod):
        if dato!=None: 
            if dato.getDato()!=c:
                cod=self.codigo(dato.getSiguiente(),c,cod)
            else:
                cod=dato.getCodigo()
        else:
            cod=False
        return cod
    def comCa2(self,pr,c):
        b=False
        if pr!=None:
            if c==pr.getDato():
                b=True
            else:
                b=self.comCa2(pr.getSiguiente(),c)
        return b
    def comCa(self,cad):
        i=0
        long=len(cad)
        b=True
        aux=self.__arreglo[1].getPrimero()
        while i<long and b==True:
            b=self.comCa2(aux,cad[i])
            i+=1
        return b
    def C(self,cad):
        b=self.codificar(cad.upper())
        if b!=None:
            print("Codigo binario resultante: ",b)
        else:
            print("Error")
    def codificar(self,cad):
        if cad.upper()==self.__arreglo[2] and self.__arreglo[6]!=None:
            print("Cadena actual, codigo=",self.__arreglo[6])
        if self.comCa(cad):
            i=0
            cod=None
            con=None
  
            aux=self.__arreglo[1].getPrimero()
            while i<len(cad):
                dig=self.codigo(aux,cad[i],cod)
                if con==None:
                    con=dig
                else:
                    con+=dig

                i+=1
            return con   
    def inicializar(self,cadena):
        for i in range(self.__cant):
            self.__arreglo[i]=None
            
        self.__arreglo[0]=cadena
        self.Mayuscula()
        self.Minuscula()
        lis=Lista_enca()
        
        ora=self.__arreglo[2]
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
 
        self.__arreglo[6]=self.codificar(self.__arreglo[2])
        #print(self.__arreglo[6])    

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
