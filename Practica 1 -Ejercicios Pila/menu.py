from PilaEncadenanda import pila
from PilaSecuencial import Pila
class menu():
    __switcher:None
    def __init__(self) -> None:
        self.__switcher={
                        '1':self.opcion1,
                        '2':self.opcion2,
                        '3':self.opcion3,
                        '4':self.opcion4

        }
    def opcion(self,op,pi):
        if type(pi)==pila or type(pi)==Pila:
            fun=self.__switcher.get(op,lambda:print("Opcion invalida"))
            if op=='1' or op=='2' or op=='3' or op=='4':
                fun(pi)
            else:
                fun()
        else:
            print("La pila no es valida")
    
    def opcion1(self,pi):
        if type(pi)==Pila:
            print("\nPila Secuencial")
        else:
            print("\nPila encadena")
        numero1 = 1
        numero2 = 2
        numero3 = 3
        numero4 = 4
      
        pi.eliminar()

        pi.insertar(numero1)
        pi.insertar(numero2)
        pi.insertar(numero3)
        pi.insertar(numero4)
        pi.insertar(numero4)
        pi.recorrer()

        print("llegue al primer eliminar")
        pi.eliminar()
        print("llegue al segundo eliminar")
        pi.eliminar()
        pi.insertar(522)
        print("Estoy recorriendo")
        pi.recorrer()
        if type(pi)==pila:
            self.opcion1(pi=Pila())

    def mostrar(self,pi):
        x=pi.eliminar()
        while x!=None:
            print(x,end='')
            x=pi.eliminar()
    
    def opcion2(self,pi):
        try:
            num=int(input("ingrese el valor que desea convertir en binario->"))
            if num>=256 and num<0:
                print("Dato no valido")
            else:
                divisor=2
                resto=0
                while num>=divisor:
                    resto=int(num%divisor)
                    pi.insertar(resto)
                    num=num//divisor
                pi.insertar(num)
                self.mostrar(pi)
        except ValueError:
            print("Se esperaba un numero")


           
    def opcion3(self,pi):
        try:
            num=int(input("Ingrese el numero a convertir->"))
            x=1
            while num>0:
                pi.insertar(num)
                num-=1
            d=pi.eliminar()
            while   d!=None:
                x*=d
                d=pi.eliminar()
            print("El factorial es",x,"!")
        except ValueError:
            print("Se esperaba un numero")

    def valido(self,dato1,dato2):
        if dato1==None or dato2==None:
            d=False
        else:
            d=dato1<dato2
        return d
    def mostrarR(self,arreglo):
        for i in range(len(arreglo)):
            d=arreglo[i]
            lis=[]
            print("\nEl estado de la lista",i+1, "es:")
            x=d.eliminar()
            while x!=None:
                lis.append(x)
                x=d.eliminar()
            j=len(lis)-1
            for i in range(len(lis)):
                print(lis[i])
                d.insertar(lis[j-i])
    def check(self,op):
        d=False
        if op>0 and op<4:
            d=True
        return d

    def opcion4(self,pi):
        import numpy as np
        arreglo=np.empty(3,dtype=Pila)
        pilaPrincipal=Pila(3)
        pilaAuxiliar=Pila(3)
        pilaFinal=Pila(3)
        pilaPrincipal.insertar(3)
        pilaPrincipal.insertar(2)
        pilaPrincipal.insertar(1)
        arreglo[0]=pilaPrincipal
        arreglo[1]=pilaAuxiliar
        arreglo[2]=pilaFinal
        cont=0
        print("Bienvenido a las torres de Hanoi.\nLas reglas son simples, debes mover todas las piesas de una torre a otra, solo puedes mover una pieza, las piezas deben ir de mayor a menor\n")
        while pilaFinal.lleno()==False:
            dis=None
            self.mostrarR(arreglo)

            print("La torre final esta vacia o incompleta, el juego continua\n")
            if pilaPrincipal.lleno()==True:
                print("La torre principal esta llena (no aceptara mas discos)")
            elif pilaAuxiliar.lleno()==True:
                print("La torre auxiliar esta llena (no aceptara mas discos)")
            try:
                op=int(input("\n Seleccione de donde desea mover la ficha Torre 1(Principal) 2(auxiliar) 3(Final)\n"))
                if self.check(op):
                    if arreglo[op-1].vacia()==True:
                        print("\n La torre",op,"esta vacia. Seleccione otra")
                    else:

                        pil=arreglo[op-1]
                        dis=pil.eliminar()
                        aux=int(input("Seleccione la torre destino, 1(Principal) 2(auxiliar) 3(Final)\n"))
                        if self.check(aux):
                            pol=arreglo[aux-1]
                            dato=pol.eliminar()
                            if dato==None:
                                pol.insertar(dis)
                                cont+=1
                            else:
                                pol.insertar(dato)
                                if self.valido(dis,dato)==True:
                                    pol.insertar(dis)
                                    cont+=1
                                else:
                                    print("No se puede ejecutar el movimiento, el disco volvio a su posicion inicial")
                                    pil.insertar(dis)
                        else:
                            print("OPcion invalida, el disco volvio a su posicion inicial")
                            pil.insertar(dis)
                else:
                    print("Opcion invalida")

            except ValueError:
                print("Se esperaba un numero")
                if dis!=None:
                    pil.insertar(dis)


        print("Felicidades resolviste el juego en",cont,"movimientos")
      





        

