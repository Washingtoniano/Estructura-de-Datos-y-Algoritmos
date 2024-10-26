from menu import menu
if __name__=='__main__':
    unmenu=menu()
    print("Bienvenido\n" )
    cadena=input("Antes de empezar, ingrese la cadena a trabajar: ")
    print("Seleccione la opcion que desea")
    try:
        op=int(" 1-Conversion a binario menidante HUffman\n 2-Transformacion en minuscula\n 3- Transformacion en minuscula\n 4-Eliminacion de un elemento\n 0-Salir\n")
        while op!=0:
            unmenu.opcion(op)
            op=int(" 1-Conversion a binario menidante HUffman\n 2-Transformacion en minuscula\n 3- Transformacion en minuscula\n 4-Eliminacion de un elemento\n 0-Salir\n")

    except ValueError():
        print("Se eesperaba un numero")