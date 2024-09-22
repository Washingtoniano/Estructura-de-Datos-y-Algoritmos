from nodo import nodo
class arbol():
    __raiz:nodo
    def __init__(self) -> None:
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
        
    def suprimir(self,arbol,dato):
        if arbol==None:
            print("No hay dato")
        else:
            d=arbol.getDato()
            if d>dato:
                
                if arbol.getIzquierda() !=None and arbol.getIzquierda().getDato()!=dato:
                    self.suprimir(arbol.getIzquierda(),dato)
                elif arbol.getIzquierda().getDato()==dato:
                    Eli=arbol.getIzquierda()
                    if Eli.getIzquierda()!=None:
                        new=Eli.getIzquierda()
                        new.setDerecha(Eli.getDerecha())
                        arbol.setIzquierda(new)
                    else:
                        arbol.setIzquierda(None)
            elif d<dato:
                if arbol.getDerecha()!=None and arbol.getDerecha().getDato()!=dato:
                    self.suprimir(arbol.getDerecha(),dato)
                elif arbol.getDerecha().getDato()==dato:
                    eli=arbol.getDerecha()
                    if eli.getDerecha()!=None:
                        new=eli.getDerecha()
                        new.setIzquierda(eli.getIzquierda())
                        arbol.setDerecha(new)
                    else:
                        arbol.setDerecha(None)
    def Buscar(self,arbol,dato):
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
    def preorden(self,arbol):
        if arbol!=None:
            print(arbol.getDato())

            self.preorden(arbol.getIzquierda())

            self.preorden(arbol.getDerecha())
    def postorden(self,arbol):
        #Iquierda derecha raiz

        if arbol!=None:

            self.postorden(arbol.getIzquierda())
            self.postorden(arbol.getDerecha())
            print(arbol.getDato())
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
        if arbol!=None:
            if arbol.getDerecha()!=None:
                d=d+1
                d=self.altura(arbol.getDerecha(),d,x)
            if arbol.getIzquierda()!=None:
                x=self.altura(arbol.getIzquierda(),d,x=x+1)
            if d>x:
                x=d
        return x


    def inorden(self,arbol):
        if arbol!=None:
            self.inorden(arbol.getIzquierda())

            print(arbol.getDato())
            self.inorden(arbol.getDerecha())
    def hoja(self,arbol,dato):
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
    def nivel(self,arbol,dato,x=0):
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


    def Hijo(self,arbol,p,H):
        Band=self.Operacion(arbol,p,H)
        if Band==True:
            print("El nodo",H,"es hijo directo del nodo",p)
        else:
            print("El nodo",H,"no es hijo directo del nodo",p)
    def Padre(self,arbol,p,H):
        Band=self.Operacion(arbol,p,H)
        if Band==True:
            print("El nodo",p,"es padre directo del nodo",H)
        else:
            print("El nodo",p,"no es padre directo del nodo",H)

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

        



            
