class menu():
    __switcher:None
    def __init__(self) -> None:
        self.__switcher={
                        '1':self.opcion1(),
                        '2':self.opcion2(),
                        '3':self.opcion3()


        }
    def opcion(self,op):
        fun=self.__switcher.get(op,lambda:print("Opcion invalida"))
        if fun=='1' or fun=='2' or fun=='3' or fun=='4':
            fun()
        else:
            fun()
    def opcion1(self): #Binario
        pass
    def opcion2(self): #Mayusucula
        pass
    def opcion3(self): #minuscula
        pass
    def opcion4(self):
        pass