from trabajo import trabajo
class menu():
    __switcher:None
    def __init__(self) -> None:
        self.__switcher={
                        '1':self.opcion1,
                        '2':self.opcion2,
                        '3':self.opcion3,
                        '4':self.opcion4


        }
    def opcion(self,op,untra):
        if type(untra)==trabajo:
            fun=self.__switcher.get(op,lambda:print("Opcion invalida"))
            if op=='1' or op=='2' or op=='3' or op=='4':
                fun(untra)
            else:
                fun()
        else:
            print("Dato no permitido")
    def inicializar(self,untra,cadena):
        untra.inicializar(cadena)
    def submenu(self,op,untra):
        if op=='1':
            print("Codigo")
            untra.MCodigo()
        elif op=='2':
            cadena=input("Ingrese una secuencia binaria\n")
            untra.deco(cadena)

    def opcion1(self,untra): #Binario:
        om=input("\n 1-Ver codigo de las letras de la cadena ingresada\n 2-Decodificar una secuencia binaria\n 0-Salir\n")
        while om!='0':
            self.submenu(om,untra)
            om=input("\n 1-Ver codigo de las letras de la cadena ingresada\n 2-Decodificar una secuencia binaria\n 0-Salir\n")


        
    def opcion2(self,untra): #Mayusucula posicion 2
        untra.Mayuscula()
    def opcion3(self,untra): #minuscula posicion 3
        untra.Minuscula()

    def opcion4(self,untra):
        cadena=input("Ingrese la cadena\n")
        untra.transformacion(cadena)
        #A considerar: cambiar una cadena alterara los datos guardados. El cambio debe ser lo mas optimo posible (revisar teoria)
        #Se puede guardar la cadena a trabajar y la anterior. Sin embargo, al realizarse el cambio, se deberan guardar tambien los datos asociados a esa cadena.
        