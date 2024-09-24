from arbol import arbol
from menu import menu

if __name__ =="__main__":
    unmenu=menu()
    ar=arbol()
    print("Bienvenido")
    op=input("Ingrese la opcion que desea\n 1-Test\n 2-\n 3-\n 0-Salir\n")
    while op != '0':
        unmenu.opcion(op,ar)
        op=input("Ingrese la opcion que desea\n 1-Test\n 2-\n 3-\n 0-Salir\n")

