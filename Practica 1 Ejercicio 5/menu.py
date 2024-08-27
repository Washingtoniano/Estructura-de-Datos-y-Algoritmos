from ColaSecuencial import ColaSecu
import random
from  ColaEncadenada import ColaEnca
class menu():
    __switcher:None
    def __init__(self):
        self.__switcher={
                        '1':self.opcion1,
                        '2':self.opcion2,
        }

    def opcion(self,op,col):
        if type(col)==ColaEnca or type(col)==ColaSecu:
            fun=self.__switcher.get(op,lambda:print("Opcion invalida"))
            if op=='1' or op== '2':
                fun(col)
            else:
                fun()
        else:
            print("Dato invalido")
    def opcion1(self,Cola):
            caj1=0
            caj2=0
            caj3=0

            tiempo=int(input("Ingrese tiempo total-> "))
            tiempo=tiempo*60
            llegada=5
            #a=random.random()

            i=0
            temp=0
            cont=0
            total=0
            x=0
            while i<tiempo:
                a=random.random()
                #print(a)

                if 0<=a<=(1/llegada):
                    Cola.insertar(i)
                    if caj1==0:
                        x=Cola.suprimir()
                        temp=i-x
                        cont+=1
                        caj1+=1
                    elif caj1!=0 and caj2==0:
                        x=Cola.suprimir()
                        temp=i-x

                        cont+=1
                        caj2+=1
                    elif caj2!=0 and caj1!=0 and caj3==0:
                        x=Cola.suprimir()
                        temp=i-x
                        cont+=1
                        caj3+=1


                if caj1==5:
                    caj1=0
                elif caj1<5:
                    caj1+=1
                if caj2==5:
                    caj2=0
                elif caj2<5:
                    caj2+=1
                if caj3==5:
                    caj3=0 
                elif caj3<5:
                    caj3+=1
                #Tiempo actual - tiempo en el que ingreso
                total=total+temp
                    
                i+=1
            print("Tiempo total de espera ",total,"min")
            print("Trabajos realizados ",cont)
            print("Tiempo promedio ",round(total/cont,2))
            print("Trabajos pendientes",Cola.getCant())



    def tiempocola(self,cola):
        x=cola.suprimir()
        d=cola.suprimir()
        while x!=None and d!=None:
            x=x+d
            d=cola.suprimir()
        if x==None:
            x=0
        return x


    def opcion2(self,cola):
        import numpy as np


        cajer1=0  #5
        col1=ColaEnca()
        cajer2=0  #3
        col2=ColaEnca()
        cajer3=0  #4
        col3=ColaEnca()

        band1=False
        band2=False
        band3=False
        llegada=2
        tiempo=2*60
        cont=0
        total=0
        tiempodeespera=0
        i=0
        while i<tiempo:
            a=random.random()
            if 0<=a<=1/llegada:
                op=0
                if col1.vacio()==True or col2.vacio()==True or col3.vacio()==True:
                    if col1.vacio()==True and col2.vacio()==True:
                        if col3.vacio()==True:
                            op=random.randint(1,3)
                        else:
                            op=random.randint(1,2)
                    elif col2.vacio()==True and col3.vacio()==True:
                        op=random.randint(2,3)
                    elif col1.vacio()==True and col3.vacio()==True:
                        op=random.choice([1,3])
                    if op!=0:
                        if op==1:
                            col1.insertar(i)
                            if cajer1==0:
                                x=col1.suprimir()
                                cont+=1                              
                                band1=True
                                tiempodeespera=i-x
                                #print(x,i)

                                #print(tiempodeespera)

                        elif op==2:
                            col2.insertar(i)
                            if cajer2==0:
                                x=col2.suprimir()
                                cont+=1
                                band2=True
                                tiempodeespera=i-x
                                #print(x,i)

                                #print(tiempodeespera)

                        else:
                            col3.insertar(i)
                            if cajer3==0:
                                x=col3.suprimir()
                                cont+=1                              
                                band3=True
                                tiempodeespera=i-x
                                #print(x,i)

                                #print(tiempodeespera)
                        total+=tiempodeespera
                else:
                    max=999
                    for i in range(3):
                        if max>col1.getCant():
                            max=col1.getCant()
                        elif max>col2.getCant():
                            max=col2.getCant()
                        elif max> col3.getCant():
                            max=col3.getCant()
                    if (max==col1.getCant()):
                        col1.insertar(i)
                    elif max==col2.getCant():
                        col2.insertar(i)
                    elif max==col3.getCant():
                        col3.insertar(i)
                    else:
                        op=random.randint(1,3)
                        if op==1:
                            col1.insertar(i)
                        elif op==2:
                            col2.insertar(i)
                        else:
                            col3.insertar(i)
            tem1=0
            tem2=0
            tem3=0

            if cajer1==0 and col1.vacio()!=True:
                    cont+=1
                    x=col1.suprimir()
                    band1=True
                    tem1=i-x

            if cajer2==0 and col2.vacio()!=True:
                    cont+=1
                    x=col2.suprimir()
                    band2=True
                    tem2=i-x

            if cajer3 ==0 and col3.vacio()!=True:
                    cont+=1
                    x=col3.suprimir()
                    band3=True
                    tem3=i-x
            total+=tem1+tem2+tem3
            if cajer1==5:
                band1=False
                cajer1=0
            elif band1==True:
                cajer1+=1
            if cajer2==3:
                band2=False
                cajer2=0
            elif band2==True:
                cajer2+=1
            if cajer3==4:
                band3=False
                cajer3 =0
            elif band3==True:
                cajer3+=1
                    
            i+=1

        print("Cantidad de clientes atendidos",cont)
        canTO=col1.getCant()+col2.getCant()+col3.getCant()
        print("Cantidad de clientes sin atender",canTO)
        print("Promedio de espera de los clientes atendidos",round(total/cont,2))
        tOTAC=self.tiempocola(col1)+self.tiempocola(col2)+self.tiempocola(col3)
        if canTO!=0:
            print("Promedio de espera de los clientes sin atender",tOTAC/canTO)
        




