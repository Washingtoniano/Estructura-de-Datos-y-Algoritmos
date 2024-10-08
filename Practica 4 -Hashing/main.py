from hash2 import hash
import random
import string
if __name__=='__main__':
    a=int(input("Ingrese las colisiones esperadas: "))
    n=int(input("Ingrese la cantidad de claves: "))
    h=hash(a,n)
    cont=0
#    for i in range(n):
#        h.insertar(i)
    
    while cont<n:
        d=random.randint(0,9)
        h.insertar(d)
        print("Cont:",cont)
        cont+=1
    print("//////")
    h.mostrar()
    for i in range (n):
        d=random.randint(0,9)
        print("Dato a buscar:",d)
        h.buscar(d)