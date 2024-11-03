from menu import menu
from trabajo import trabajo
if __name__=='__main__':
    unmenu=menu()
    untrabajo=trabajo()
    print("Bienvenido\n" )
    cadena=input("Antes de empezar, ingrese la cadena a trabajar: ")
    unmenu.inicializar(untrabajo,cadena)

    print("Seleccione la opcion que desea")
    
    op=input(" 1-Conversion a binario mediante HUffman\n 2-Transformacion en mayuscula\n 3-Transformacion en minuscula\n 4-Eliminacion de un elemento\n 0-Salir\n")
    while op!='0':
        unmenu.opcion(op,untrabajo)
        op=input(" 1-Conversion a binario mediante HUffman\n 2-Transformacion en mayuscula\n 3-Transformacion en minuscula\n 4-Eliminacion de un elemento\n 0-Salir\n")

