class lista():
    __primero:object
    __cant:object
    __ultimo:object
    def __init__(self):
        self.__primero =None
        self.__cant=0
        self.__ultimo=None
    def vacio(self):
        return self.__cant==0
    def insertar(self,hoja):
        if self.vacio()==True:
            self.__primero=hoja
            self.__ultimo=hoja
        else:
            longP=len(self.__primero.getCodigo())
            longH=len(hoja.getCodigo())
            if longP>longH:
                aux=self.__primero
                ant=aux
                while aux!=None and len(aux.getCodigo())>longH:
                    ant=aux
                    aux=aux.getSiguiente()
                hoja.setSiguiente(aux)
                ant.setSiguiente(hoja)
                if aux==None:
                    self.__ultimo=hoja
            else:
                hoja.setSiguiente(self.__primero)
                self.__primero=hoja

        self.__cant+=1
    def getCant(self):
        return self.__cant
    def mostrar(self):
        aux=self.__primero
        while aux!=None:

            print(aux)
            aux=aux.getSiguiente()
    def getPrimero(self):
        return self.__primero

