from arbol import arbol
def test():
    ar=arbol()
    x=ar.getraiz()
    ar.insertar(x,5)
    x=ar.getraiz()
    ar.insertar(x,3)
    ar.insertar(x,1)
    ar.insertar(x,4)
    ar.insertar(x,2)
    ar.suprimir(x,4)
    ar.preorden(x)
    print("_______")
    ar.postorden(x)
    print("_____")
    ar.inorden(x)


if __name__ =="__main__":
    test()