from Lista_Encadenada import ListEnca
from Lista_Secuencial import ListSecu
from menu import menu
def test():
    Ls=ListEnca()
    print("PRueba")
    # Ls.insertar(1,0)
    # Ls.insertar(2,1)
    # Ls.insertar(3,0)
    # Ls.insertar(4,2)
    # Ls.insertar(5,1)
    Ls.InsertarPorContenido(3)
    Ls.InsertarPorContenido(5)
    Ls.InsertarPorContenido(1)
    Ls.InsertarPorContenido(4)
    Ls.InsertarPorContenido(2)
    Ls.Recorrer()
    print("____")

    Ls.SuprimirPorContenido(3)

    Ls.Recorrer()
    
    print("____")
    # Ls.Suprimir(2)
    # Ls.Recorrer()
    # Ls.Buscar(2)
    # print("____")
    Ls.Primero()
    Ls.Ultimo()
    print("El Anterior de {} es {}".format(1,Ls.Anterior(1)))
    print("El Siguiente de {} es {}".format(2,Ls.Siguiente(2)))
  


if __name__ =="__main__":
    #test()
    unmenu=menu()
    print("Bienvenido")
    op=input("Ingrese la opcion que desea\n 1-Matriz\n 2-Polinomio\n 3-Head\n 0-Salir\n")
    while op!='0':
        unmenu.opcion(op)
        op=input("Ingrese la opcion que desea\n 1-Matriz\n 2-Polinomio\n 3-Head\n 0-Salir\n")
    print("Adios")
