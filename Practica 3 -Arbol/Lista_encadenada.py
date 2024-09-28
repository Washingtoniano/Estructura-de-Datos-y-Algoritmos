from caracter import caracter
#Lista der arboles
class Lista_enca():
    __primero:object
    __ultimo:object
    __cant:int
    
    def __init__(self):
        self.__primero=None
        self.__ultimo=None
        self.__cant=0
    def Vacio(self):
        return self.__cant==0
    def insertar(self,nodo):
        if self.Vacio()==True:
            self.__primero=nodo
            self.__ultimo=nodo
        else:
            if self.__primero.getFrecuencia()>nodo.getFrecuencia():
                nodo.setSiguiente(self.__primero)
                self.__primero=nodo
            else:
                aux=self.__primero
                ant=aux
                while aux!=None and aux.getFrecuencia()<=nodo.getFrecuencia():
                    ant=aux
                    aux=aux.getSiguiente()
                if aux==None:
                    ant.setSiguiente(nodo)
                    self.__ultimo=nodo
                else:
                    nodo.setSiguiente(ant.getSiguiente())
                    ant.setSiguiente(nodo)

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
                    


