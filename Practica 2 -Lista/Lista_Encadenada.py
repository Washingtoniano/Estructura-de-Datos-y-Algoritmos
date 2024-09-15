from nodo import Nodo
class ListEnca():
    __comienzo:Nodo
    __cant:int
    __ultimo:Nodo
    
    def __init__(self) -> None:
        self.__comienzo=None
        self.__cant=0
        self.__ultimo=None
    def Vacio(self):
        return self.__cant==0
    def insertar(self,dato,pos=0):
        unnodo=Nodo(dato)
        if pos>=0 and pos<=self.__cant:
            if pos==0:
                unnodo.setSiguiente(self.__comienzo)
                self.__comienzo.setSiguiente(unnodo)
            else:
                i=0
                aux=self.__comienzo
            
                anterior=aux
                while i<pos and aux!=None:
                    anterior=aux
                    aux=aux.getSiguiente()
                    i+=1
                if aux==None:
                    self.__ultimo=unnodo
                unnodo.setSiguiente(aux)
                anterior.setSiguiente(unnodo)


    def Recuperar(self,pos):
        if self.Vacio()!=True:
            if pos>=0 and pos<self.__cant:
                dato=False
                if pos==0:
                    dato=self.__comienzo.getDato()
                else:
                    con=0
                    aux=self.__comienzo
                    while aux.getSiguiente()!=None and con!=pos:
                        aux=aux.getSiguiente()
                        con+=1
                    if aux!=None:
                        dato=aux.getDato()
                        print("En la posicion",pos,"se encuentra el numero",dato)
            else:
                print("Posicion invalida")
        else:
            print("Dato invalido")
    def Suprimir(self,pos):
        if self.Vacio()!=True:
            if pos>=0 and pos<self.__cant:
                if pos==0:
                    self.__comienzo=self.__comienzo.getSiguiente()
                    self.__cant-=1
                else:
                    aux=self.__comienzo
                    anterior=aux
                    con=0
                    while aux!=None and con !=pos:
                        anterior=aux
                        aux=aux.getSiguiente()
                        con+=1
                    anterior.setSiguiente(aux.getSiguiente())
                    print("Se elmino el dato",aux.getDato(),"en la posicion",con)
                    self.__cant-=1
            else:
                print("Posicion invalida")
        else:
            print("Lista vacia")

    def Primero(self):
        if not self.Vacio():
            print ("Primero",self.__comienzo.getDato())
        else:
            print("Lista vacia")
    def Ultimo(self):
        if not self.Vacio():
            print( "Ultimo",self.__ultimo.getDato())
        else:
            print("Lista vacia")
    def Buscar(self,dato):
        if not self.Vacio():
            aux=self.__comienzo
            while aux!=None and aux.getDato()!=dato:
                aux=aux.getSiguiente()
            if aux.getDato()==dato:
                print("El dato",dato,"esta en la lista")
            else:
                print("No se encontro el dato")
        else:
            print("Lista vacia")

            
    def Anterior(self,pos):
        if not self.Vacio():
            if pos>=0 and pos<self.__cant:
                if pos==0:
                    print("El elemento en la posicion",pos,"es el primero, no tienen anterir")
                else:
                    aux=self.__comienzo
                    con=0
                    anterior=aux
                    while aux!=None and pos!=con:
                        anterior=aux
                        aux=aux.getSiguiente()
                        con+=1
                    return anterior.getDato()
            else:
                print("Valor invalido")
                    
        else:
            print("Lista vacia")


    def Siguiente(self,pos):
        if not self.Vacio():
            if pos>=0 and pos<self.__cant:
                if pos==self.__cant-1:
                    print("El elemento en la posicion",pos,"es el ultimo, no tienen siguiente")
                else:
                    aux=self.__comienzo
                    con=0
                    while aux!=None and pos!=con:
                        aux=aux.getSiguiente()
                        con+=1
                    return aux.getSiguiente().getDato()
            else:
                print("Valor invalid")
                    
        else:
            print("Lista vacia")
    
    def InsertarPorContenido(self,dato):
        unnodo=Nodo(dato)
        if self.Vacio()==True:
            self.__comienzo=unnodo
            self.__ultimo=unnodo
            
        elif self.__comienzo.getDato()>dato:
            unnodo.setSiguiente(self.__comienzo)
            self.__comienzo=unnodo
        
        else:
            aux=self.__comienzo
            anterior=aux
            while aux!=None and aux.getDato()<dato:
                anterior=aux
                aux=aux.getSiguiente()
            if aux==None:
                anterior.setSiguiente(unnodo)
                self.__ultimo=unnodo
            else:
                unnodo.setSiguiente(anterior.getSiguiente())
                anterior.setSiguiente(unnodo)
        self.__cant+=1

    def Recorrer(self):
        if not self.Vacio():
            aux=self.__comienzo
            while aux!=None:
                print(aux.getDato())
                aux=aux.getSiguiente()
        else:
            print("Lista vacia")
    def SuprimirPorContenido(self,dato):
        if not self.Vacio():
            if self.__comienzo.getDato()==dato:
                self.__comienzo=self.__comienzo.getSiguiente()
                self.__cant-=1
            else:
                aux=self.__comienzo
                anterior=aux
                while aux!=None and aux.getDato()!=dato:
                    anterior=aux
                    aux=aux.getSiguiente()
                if aux!=None:
                    x=aux.getDato()
                    anterior.setSiguiente(aux.getSiguiente())
                    print("Se elmino el dato",x,"de la lista")
                    self.__cant-=1
                else:
                    print("El dato no se encontro")
        else:
            print("Lista vacia")



            
    




