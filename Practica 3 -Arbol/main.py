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
    ar.insertar(x,6)
    print("______")
    ar.Hijo(x,5,6)
    ar.Padre(x,5,6)
    ar.camino(x,6,1)
    print("_____")
    ar.insertar(x,0)
    ar.suprimir(x,4)
    print("______")
    print("Preorden")
    ar.preorden(x)
    print("_______")
    print("Postorden")
    ar.postorden(x)
    print("_____")
    print("Inorden")
    ar.inorden(x)
    print("Raiz",ar.getraiz())
    print("la altura del arbol es de ",ar.altura(x))


if __name__ =="__main__":
    test()