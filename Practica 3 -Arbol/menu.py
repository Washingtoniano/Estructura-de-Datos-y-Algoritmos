from caracter import caracter
from Lista_encadenada import Lista_enca
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
        ar=arbol()
        ar.insertar(ar.getraiz(),5)
        ar.insertar(ar.getraiz(),3)
        ar.insertar(ar.getraiz(),1)
        ar.insertar(ar.getraiz(),4)
        ar.insertar(ar.getraiz(),2)
        ar.insertar(ar.getraiz(),6)
        ar.insertar(ar.getraiz(),0)
        ar.insertar(ar.getraiz(),8)
        ar.insertar(ar.getraiz(),7)
        ar.insertar(ar.getraiz(),9)
        
        self.test(ar)


    
    def test(self,ar):
        x=ar.getraiz()

        print("Datos insertados: 5314260879")

        print("______")
        ar.Hijo(x,5,6)
        ar.Padre(x,5,6)
        ar.camino(x,6,1)
        print("_____")
        borrar=0
        try:
            borrar=int(input("Ingrese el dato a borrar "))
        except ValueError:
            print("Se esperaba un numero")
        if ar.Buscar(x,borrar):
            ar.suprimir(x,borrar)
            print("Dato borrado:",borrar)

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
        ar.reset()   

    def opcion2(self,arb):
        ar=arbol()
        ar.insertarIterativo(5)
        ar.insertarIterativo(3)
        ar.insertarIterativo(1)
        ar.insertarIterativo(4)
        ar.insertarIterativo(2)
        ar.insertarIterativo(6)
        ar.insertarIterativo(0)
        ar.insertarIterativo(8)
        ar.insertarIterativo(7)
        ar.insertarIterativo(9)
        self.test(ar)



    def opcion3(self,ar):
        #Usar lista ordenada, modificar el nodo con caracter y lista de arboles
        ora=input("Ingrese una oracion ")
        self.generacion(ar,ora)
        print("Arbol generado")
        print(" MUESTRA EN INORDEN ")
        ar.inorden(ar.getraiz())
        print("\n --------------------")
        print("\n MUESTRA EN POSTORDEN ")
        ar.postorden(ar.getraiz())
        print(" --------------------")
        print("\n MUESTRA EN PREORDEN ")
        ar.preorden(ar.getraiz())
        op=input("Que desea hacer")
    def generacion(self,ar,ora):
        lis=Lista_enca()
        d=0
        j=0
        lon=len(ora)
        for d in range(lon):
            uncaracter=caracter()
            uncaracter.setCaracter(ora[d])
            cont=0
            for j in range(lon):
                if ora[d]==ora[j]:
                    cont+=1
            uncaracter.setFrecuencia(cont)
            lis.insertar(uncaracter)
        while lis.Uno()!=True:
            primero=lis.Suprimir(lis.Primero())
            segundo=lis.Suprimir(lis.Primero())
            total=primero+segundo
            uncaracter=caracter()
            uncaracter.setFrecuencia(primero.getFrecuencia()+segundo.getFrecuencia())
            if ar.vacio()==True:
                uncaracter.setCaracter(total)

                ar.setRaiz(uncaracter)
            else:
                a=ar.getraiz().getDato()
                total+=a.getCaracter()
                uncaracter.setCaracter(total)

                ar.setRaiz(uncaracter)
            ar.insertar(ar.getraiz(),segundo)
            ar.insertar(ar.getraiz(),primero)
            if lis.Uno()==False:
                lis.insertar(ar.getraiz().getDato())
        if lis.Uno()==True:
            ar.setRaiz(lis.Suprimir(lis.Primero()))
        for i in range(lon):
            ar.Codigos(ar.getraiz(),ora[i])
       


            