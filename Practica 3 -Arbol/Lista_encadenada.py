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
                while aux!=None and aux.getFrecuencia()<car.getFrecuencia():
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

    def restar(self):
        self.__primero =None
        self.__ultimo=None
        self.__cant=0
