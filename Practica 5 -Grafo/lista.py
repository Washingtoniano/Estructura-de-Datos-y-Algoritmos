from nodo import nodo
class lista():
    __comienzo:nodo
    __cant:int
    __ultimo:nodo
    def __init__(self):
        self.__comienzo=None
        self.__cant=0
        self.__ultimo=None
    def insertar(self,n):
        unnodo=nodo(n)
        if self.__comienzo==None:
            unnodo.setSig(self.__comienzo)
            self.__comienzo=unnodo
        else:
            aux=self.__comienzo
            while aux.getSig()!=None:
                aux=aux.getSig()
            unnodo.setSig(aux.getSig())
            aux.setSig(unnodo)
        self.__ultimo=unnodo
        self.__cant+=1
    
    def eliminar(self):
        aux=self.__comienzo
        ant=aux
        while aux.getSig()!=None:
            ant=aux
            aux=aux.getSig()
        ant.setSig(None)
        self.__cant-=1
    def primero(self):
        return self.__comienzo.getDato()
    def comprobar(self,j):
        b=False
        aux=self.__comienzo
        if j==0:
            if self.__comienzo.getDato()-1==j:
                b=True
        else:
            for i in range (j):
                aux=aux.getSig()
            if aux!=None and aux.getDato()-1==j:
                b=True
        return b
    def mostrar(self):
        aux=self.__comienzo
        i=0
        while aux!=None:
            print(aux.getDato(),end=' ')
            aux=aux.getSig()
        print("\n")
    def reset(self):
        self.__comienzo=None
    def getUltimo(self):
        return self.__ultimo.getDato()



        
