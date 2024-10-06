from nodo import nodo
class arbol():
    __raiz:nodo
    def __init__(self) -> None:
        self.__raiz=None
    def reset(self):
        self.__raiz=None
    def vacio(self):
        return self.__raiz==None
    def insertar(self,arbol,dato):
        unnodo=nodo(dato)
        if self.vacio()==True:
            self.__raiz=unnodo
        elif arbol.getDato()==dato:
            print("Dato ya ingresado")
        elif arbol.getDato()>dato:
            if arbol.getIzquierda()==None:
                arbol.setIzquierda(unnodo)
            else:
                self.insertar(arbol.getIzquierda(),dato)
        elif arbol.getDato()<dato:
            if arbol.getDerecha()==None:
                arbol.setDerecha(unnodo)
            else:
                self.insertar(arbol.getDerecha(),dato)
    def getraiz(self):
        return self.__raiz
    def insercion_eli(self,Eli): #Obtener el nuevo nodo que reempazara al eliminado
        new=None
        if Eli!=None:
            if Eli.getGrado()==2:
                new=self.mayor(Eli.getIzquierda())
                new.setDerecha(Eli.getDerecha())
                if Eli.getIzquierda().getDato()!=new.getDato():
                    new.setIzquierda(Eli.getIzquierda())
            elif Eli.getGrado()==1:
                    if Eli.getDerecha()!=None:
                        new=Eli.getDerecha()

                    else:
                        new=Eli.getIzquierda()
        return new

    def suprimir(self,arbol,dato):
        #Comprobar myor de menores, se puede reutilizar el codigo menor para los demas casos, buscando hojas y convirtiendolas en reemplazos del nodo a eliminar 
        if self.vacio()==False:
            if arbol==None:
                print("No hay dato")
            else:
                d=arbol.getDato()
                if d>dato:
                    if arbol.getIzquierda() !=None and arbol.getIzquierda().getDato()!=dato:
                        self.suprimir(arbol.getIzquierda(),dato)
                    elif arbol.getIzquierda().getDato()==dato:
                        Eli=arbol.getIzquierda()
                        new=self.insercion_eli(Eli)
                        arbol.setIzquierda(new)        
                elif d<dato:
                    if arbol.getDerecha()!=None and arbol.getDerecha().getDato()!=dato:
                        self.suprimir(arbol.getDerecha(),dato)
                    elif arbol.getDerecha().getDato()==dato:
                        Eli=arbol.getDerecha()
                        new=self.insercion_eli(Eli)

                        arbol.setDerecha(new)
                elif d==dato:
                        
                    Eli=self.__raiz

                    new=self.insercion_eli(Eli)
                    self.__raiz=new

        else:
            print("Arbol vacio")

    def mayor(self,ar):
        aux=None

        while ar.getDerecha()!=None:
            aux=ar
            ar=ar.getDerecha()

        maxi=ar
        if aux!=None:
            aux.setDerecha(None)
        return maxi



    def Buscar(self,arbol,dato):
        if self.vacio()==False:
        #Se pueden borrar el primer if y el print
            a=False
            if arbol==None:
                print("Dato inexistente")
            elif arbol.getDato()==dato:
                a=True
            elif arbol.getDato()<dato:
                a=self.Buscar(arbol.getDerecha(),dato)
            elif arbol.getDato()>dato:
                a=self.Buscar(arbol.getIzquierda(),dato)
            return a
        else:
            print("Arbol vacio")
    def preorden(self,arbol):
        if self.vacio()==False:
            if arbol!=None:
                print(arbol.getDato())

                self.preorden(arbol.getIzquierda())

                self.preorden(arbol.getDerecha())
        else:
            print("Arbol vacio")
    def postorden(self,arbol):
        #Iquierda derecha raiz
        if self.vacio()==False:

            if arbol!=None:

                self.postorden(arbol.getIzquierda())
                self.postorden(arbol.getDerecha())
                print(arbol.getDato())
        else:
            print("Arbol vacio")
    # def altura(self,arbol,de=0,iz=0):
    #     if arbol !=None:
    #         if arbol.getDerecha()!=None:
    #             x=de+1
    #             de=self.altura(arbol.getDerecha(),x,iz)
    #         if arbol.getIzquierda()!=None:
    #             y=iz+1
    #             iz=self.altura(arbol.getIzquierda(),de,y)
    #         if de<iz:
    #             de=iz
    #         return de
        
            
            
    def altura(self,arbol,d=0,x=0):
        if self.vacio()==False:
            if arbol!=None:
                if arbol.getDerecha()!=None:
                    d=d+1
                    d=self.altura(arbol.getDerecha(),d,x)
                if arbol.getIzquierda()!=None:
                    x=self.altura(arbol.getIzquierda(),d,x=x+1)
                if d>x:
                    x=d
            return x
        else:
            print("Arbol vacio")


    def inorden(self,arbol):
        if self.vacio()==False:
            if arbol!=None:
                self.inorden(arbol.getIzquierda())

                print(arbol.getDato())
                self.inorden(arbol.getDerecha())
        else:
            print("Arbol vacio")
    def hoja(self,arbol,dato):
        if self.vacio()==False:
            if arbol==None:
                print("Error")
            elif arbol.getDato()==dato:
                if arbol.getDerecha()==None and arbol.getIzquierda()==None:
                    print("Es una hoja")
                else:
                    print("No es una hoja")
            elif arbol.getDato()>dato:
                self.hoja(arbol.getIzquierda(),dato)
            elif arbol.getDato()<dato:
                self.hoja(arbol.getDerecha(),dato)
        else:
            print("Arbol vacio")
    def nivel(self,arbol,dato,x=0):
        if self.vacio()==False:
            if arbol==None:
                print("Error")
            elif arbol.getDato()==dato:
                print("El nodo",dato,"se encuentra en el nivel",x)
            elif arbol.getDato()<dato:
                x+=1
                self.nivel(arbol.getDerecha(),dato,x)
            elif arbol.getDato()>dato:
                x+=1
                self.nivel(arbol.getIzquierda(),dato,x)
        else:
            print("Arbol vacio")


    def Hijo(self,arbol,p,H):
        if self.vacio()==False:
            Band=self.Operacion(arbol,p,H)
            if Band==True:
                print("El nodo",H,"es hijo directo del nodo",p)
            else:
                print("El nodo",H,"no es hijo directo del nodo",p)
        else:
            print("Arbol vacio")
    def Padre(self,arbol,p,H):
        if self.vacio()==False:
            Band=self.Operacion(arbol,p,H)
            if Band==True:
                print("El nodo",p,"es padre directo del nodo",H)
            else:
                print("El nodo",p,"no es padre directo del nodo",H)
        else:
            print("Arbol vacio")

    def Operacion(self,arbol,P,H):
        band=False
        if self.vacio()==False:
            if arbol!=None:
                if arbol.getDato()==P:
                    if arbol.getIzquierda().getDato()==H or arbol.getDerecha().getDato()==H:
                        band=True
                elif arbol.getDato()<P:
                    self.padre(arbol.getDerecha(),P,H)
                elif arbol.getDato()>P:
                    self.padre(arbol.getIzquierda(),P,H)
        else:
            print("Vacio")
        return band

    def listar(self,arbol,B,lista):
        Dato=False
        if arbol!=None:
            Dato=lista
            if arbol.getDato()!=B:
                lista.append(arbol.getDato())
                if arbol.getDato()<B:
                    Dato=self.listar(arbol.getDerecha(),B,lista)
                elif arbol.getDato()>B:
                    Dato=self.listar(arbol.getIzquierda(),B,lista)
            else:
                lista.append(B)
        return Dato


    def camino(self,arbol,A,B):
        if self.vacio()==False:
            if arbol!=None:
                if arbol.getDato()==A:
                    lista=[]
                    Band=self.listar(arbol,B,lista)
                    if Band!=False:
                        print("El camino del nodo",A,"al nodo",B,"es:")
                        i=0
                        while i< len(lista):
                            print(lista[i],end='')
                            i+=1
                        print(".")
                    else:
                        print("No hay camino posible de",A,"a",B)
                elif arbol.getDato()<A:
                    self.camino(arbol.getDerecha(),A,B)
                elif arbol.getDato()>A:
                    self.camino(arbol.getIzquierda(),A,B)
            else:
                print("Error")
        else:
            print("Arbol Vacio")

    def insertarIterativo(self,dato):
        band=False

        unnodo=nodo(dato)
        if self.vacio()==True:
            self.__raiz=unnodo
        else:
            aux=self.getraiz()
            BD=False
            BI=False
            while aux!=None and band==False:
                ant=aux
                D=aux.getDato()
                if D==dato:
                    band==True
                else:
                    if D>dato:
                        aux=aux.getIzquierda()
                        BD=False
                        BI=True
                    elif D<dato:
                        aux=aux.getDerecha()
                        BD=True
                        BI=False
                    if aux==None:
                        if BD==True:
                            ant.setDerecha(unnodo)
                        elif BI ==True:
                            ant.setIzquierda(unnodo)
        if band==True:
            print("Dato ya ingresado")
        else:
            print("Dato cargado")

    def restart(self):
        self.__raiz=None
   
    def setRaiz(self,dato):
        unnodo=nodo(dato)

        if self.vacio()==True:
            self.__raiz=unnodo
        else:
            if unnodo.getDato()<self.__raiz:
                unnodo.setDerecha(self.__raiz)
                self.__raiz=unnodo
            elif unnodo.getDato()>self.__raiz:
                unnodo.setIzquierda(self.__raiz)
                self.__raiz=unnodo
    def Codigos(self,arbol,c):
        if self.vacio()!=True:
            if arbol!=None:
                dato=c.getDato()
                izq=False
                der=False

                if arbol!=c:
                    i=arbol.getIzquierda().getDato()
                    j=0
                    while j<len(i) and izq==False:
                        if i[j]==dato:
                            izq=True
                        j+=1
                    if izq==True:
                        c.setCodigo(0)
                        self.Codigos(arbol.getIzquierda(),c)
                    else:
                        d=arbol.getDerecha().getDato()

                        j=0
                        while j<len(d) and der==False:
                            if d[j]==dato:
                                der=True
                            j+=1
                        if der==True:
                            c.setCodigo(1)
                            self.Codigos(arbol.getDerecha(),c)
                else:
                    cod=c.getCodigo()
                    for i in range (len(cod)):
                        arbol.setCodigo(cod[i])






            
