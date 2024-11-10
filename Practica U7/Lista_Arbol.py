from caracter import caracter
#Lista der arboles
#Lista de arboles generada por los nodos(no hace uso de la clase arbol)
class Lista_enca():
    __primero:caracter
    __ultimo:caracter
    __cant:int
    
    def __init__(self):
        self.__primero=None
        self.__ultimo=None
        self.__cant=0
    def Vacio(self):
        return self.__cant==0
    def insertar(self,car):
        if self.Vacio()==True:
            self.__primero=car
            self.__ultimo=car
        else:
            if self.__primero.getFrecuencia()>car.getFrecuencia():
                car.setSiguiente(self.__primero)
                self.__primero=car
            else:
                aux=self.__primero
                ant=aux
                #menor o menor igual?
                while aux!=None and aux.getFrecuencia()<=car.getFrecuencia():
                    ant=aux
                    aux=aux.getSiguiente()
                if aux==None:
                    ant.setSiguiente(car)
                    self.__ultimo=car
                else:
                    car.setSiguiente(ant.getSiguiente())
                    ant.setSiguiente(car)

        self.__cant+=1
    def Uno(self):
        return self.__cant==1
    def Primero(self):
        if self.Vacio()!=True:
            return self.__primero

    def Suprimir(self,dato):
        borrado=None
        if self.Vacio()!=True:
            if self.__primero==dato:
                borrado=self.__primero
                self.__primero=self.__primero.getSiguiente()
                self.__cant-=1
            else:
                aux=self.__primero
                anterior=aux
                while aux!=None and aux!=dato:
                    anterior=aux
                    aux=aux.getSiguiente()
                if aux!=None:
                    borrado=aux
                    anterior.setSiguiente(aux.getSiguiente())
                    self.__cant-=1
            return borrado
        else:
            print("Lista vacia")
    def Buscar(self,dato):
        if self.Vacio()==False:
            band=False
            aux=self.__primero
            while aux!=None and aux!=dato:
                aux=aux.getSiguiente()
            if aux!=None:
                band=True
            return band
                    
    def mostrar(self,arbol):
        if self.Vacio()==False:
            if arbol!=None:
                self.mostrar(arbol.getIzquierda())

                (arbol.mostrar())
                self.mostrar(arbol.getDerecha())
        else:
            print("Arbol vacio")
    
    def Codigos(self,arbol,c):
        #Probar utilizar el largo de la cadena, para evitar el error del NONE
        if self.Vacio()!=True:
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
    def Codigo(self,arbol,c,cod):
        #Probar utilizar el largo de la cadena, para evitar el error del NONE
        if self.Vacio()!=True:
            if arbol!=None:
                dato=c
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
                        if cod==None:
                            cod='0'
                        else:
                            cod+='0'
                        cod=self.Codigo(arbol.getIzquierda(),c,cod)
                    else:
                        d=arbol.getDerecha().getDato()

                        j=0
                        while j<len(d) and der==False:
                            if d[j]==dato:
                                der=True
                            j+=1
                        if der==True:
                            if cod==None:
                                cod='1'
                            else:
                                cod+='1'
                            cod=self.Codigo(arbol.getDerecha(),c,cod)
            return(cod)


    def decodifcar(self,arbol,cod,i):
    
        p=len(cod)
        band=False
        con=p
        while  p> i and band==False :
                ant=arbol
                d=i+1
                if p-1==i:
                    d=i
              #  print(cod[d])
                if cod[d]!='1' and cod[d]!='0':
                        print("Dato no binario")
                        band=True
                else:
                    if len(ant.getDato())!=1:
                            if  cod[d]=='0':
                                arbol=arbol.getIzquierda()

                            elif  cod[d]=='1': 
                                arbol=arbol.getDerecha()
                            i+=1 
                          
                    else:
                        print (ant.getDato())
                        con-=1
                if p> i and len(ant.getDato()) ==1:
                    arbol=(self.Primero())
       # print(arbol.getDato())
    def getCant(self):
        return self.__cant
    def hojas(self,arbol,l):
        if arbol!=None:
            if arbol.grado()==0:
                ne=arbol
                ne.setSiguiente(None)
                l.insertar(ne)
            self.hojas(arbol.getIzquierda(),l)

            self.hojas(arbol.getDerecha(),l)
                                
    def restar(self):
        self.__primero =None
        self.__ultimo=None
        self.__cant=0
