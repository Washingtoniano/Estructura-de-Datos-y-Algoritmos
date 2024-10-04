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
            if ar.Buscar(x,borrar):
                ar.suprimir(x,borrar)
                print("Dato borrado:",borrar)
        except ValueError:
            print("Se esperaba un numero")
   


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

    def opcion2(self,ar):
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
        lis=Lista_enca()

        ora=input("Ingrese una oracion ")
        ora=ora.upper()
        self.generacion(ar,ora,lis)
        print("Arbol generado")
        print(" MUESTRA EN INORDEN ")
        raiz=ar.getraiz().getDato()
        ar.inorden(raiz)
        print("\n --------------------")
        print("\n MUESTRA EN POSTORDEN ")
        ar.postorden(raiz)
        print(" --------------------")
        print("\n MUESTRA EN PREORDEN ")
        ar.preorden(raiz)
        op=input("¿Desea mostrar su codificacion en binario?\n Y o N\n")
        while op.upper()!='N' and op.upper()!='Y':
            print ("Opcion invalida")
            op=input("¿Desea mostrar su codificacion en binario?\n Y o N\n")

        if op.upper()=='Y':
            lon=len(ora)
            for i in range (lon):
                fre=self.frecuencia(lon,ora,ora[i])
                ar.Codigos(raiz,ora[i],fre)
                lis.mostrar()
    
    def frecuencia(self,long,ora,d):

        cont=0
        for i in range (long):
            if d==ora[i]:
                cont+=1
        return cont
            
    def generacion(self,ar,ora,lis):
        long=len(ora)
        for i in range(long):
            uncaracter=caracter(ora[i])
            cont=self.frecuencia(long,ora,ora[i])
       
            uncaracter.setFrecuencia(cont)
            if lis.Buscar(uncaracter)==False or lis.Vacio()==True:
  
                lis.insertar(uncaracter)
        while lis.Uno()==False:
            primero=lis.Suprimir(lis.Primero())
            segundo=lis.Suprimir(lis.Primero())
            #print(primero.getCaracter())
            #print(segundo.getCaracter())

            nuevo=caracter(primero.getDato()+segundo.getDato())
            nuevo.setIzquierda(primero)
            nuevo.setDerecha(segundo)
          
            fre=primero.getFrecuencia()+segundo.getFrecuencia()


            nuevo.setFrecuencia(fre)
            lis.insertar(nuevo)
        ar.setRaiz(lis.Primero())


            