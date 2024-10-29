from trabajo import trabajo
class menu():
    __switcher:None
    def __init__(self) -> None:
        self.__switcher={
                        '1':self.opcion1(),
                        '2':self.opcion2(),
                        '3':self.opcion3()


        }
    def opcion(self,op,untra):
        if type(untra)==trabajo:
            fun=self.__switcher.get(op,lambda:print("Opcion invalida"))
            if fun=='1' or fun=='2' or fun=='3' or fun=='4':
                fun(untra)
            else:
                fun()
        else:
            print("Dato no permitido")
    def opcion1(self,untra): #Binario
        pass
    def opcion2(self,untra): #Mayusucula
        pass
    def opcion3(self,untra): #minuscula
        pass
    def opcion4(self,untra):
        pass