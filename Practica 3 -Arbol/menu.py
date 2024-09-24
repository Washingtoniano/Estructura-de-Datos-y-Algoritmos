from arbol import arbol
class menu():
    __switcher:None
    def __init__(self) -> None:
        self.__switcher={
                '1':self.opcion1,
                '2':self.opcion2,
                '3':self.opcion3,
        }
    def opcion(self,op,ar):
        if type(ar)==arbol:
            fun=self.__switcher.get(op,lambda:print("Opcion invalida"))
            if op=='1' or op =='2' or op =='3':
                fun(ar)

            else:
                fun()
        else:
            print("No hay arbol")
    def opcion1(self,ar):
        x=ar.getraiz()
        ar.insertar(ar.getraiz(),5)
        x=ar.getraiz()
        ar.insertar(ar.getraiz(),3)
        ar.insertar(ar.getraiz(),1)
        ar.insertar(ar.getraiz(),4)
        ar.insertar(ar.getraiz(),2)
        ar.insertar(ar.getraiz(),6)
        ar.insertar(ar.getraiz(),0)

        print("Datos insertados: 5314260")

        print("______")
        ar.Hijo(x,5,6)
        ar.Padre(x,5,6)
        ar.camino(x,6,1)
        print("_____")
        ar.suprimir(x,3)
        print("Dato borrado :3")
        print("______")
        print("Preorden")
        ar.preorden(ar.getraiz())
        print("_______")
        print("Postorden")
        ar.postorden(ar.getraiz())
        print("_____")
        print("Inorden")
        ar.inorden(ar.getraiz())
        print("Raiz",ar.getraiz().getDato())
        print("la altura del arbol es de ",ar.altura(x))
        print("Buscar nodo 3",ar.Buscar(x,3))
        if ar.Buscar(ar.getraiz(),9)==True:
            print("Se encontro el dato")

    def opcion2(self,ar):
        pass
    def opcion3(self,ar):
        pass