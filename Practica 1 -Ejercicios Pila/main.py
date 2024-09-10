from menu import menu
from PilaEncadenanda import pila
from PilaSecuencial import Pila

def test():
    
    numero1 = 1
    numero2 = 2
    numero3 = 3
    numero4 = 4

    pila = Pila(4)
    pila.eliminar()

    pila.insertar(numero1)
    pila.insertar(numero2)
    pila.insertar(numero3)
    pila.insertar(numero4)
    pila.insertar(numero4)
    pila.recorrer()

    print("llegue al primer eliminar")
    pila.eliminar()
    print("llegue al segundo eliminar")
    pila.eliminar()
    pila.insertar(522)
    print("Estoy recorriendo")
    pila.recorrer()


if __name__ == '__main__':
    unmenu=menu()
    unapila=pila()
    print("Bienvenido\n")
    op=input("Ingrese la opcion que desea\n 1-Probar pila\n 2-Convertir a binario\n 3-Obtener Factorial\n 4-Juego de torres\n 0-Salir\n")
    while op!='0':
        unmenu.opcion(op,unapila)
        op=input("\nIngrese la opcion que desea\n 1-Probar pila\n 2-Convertir a binario\n 3-Obtener Factorial\n 4-Juego de torres\n 0-Salir\n")

    #test()
    

