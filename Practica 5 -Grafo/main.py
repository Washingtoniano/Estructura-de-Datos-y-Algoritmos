from grafo import grafo
if __name__=='__main__':
    ver=int(input("Ingrese cantidad de vertices: "))
    ungrafo=grafo(ver)

    print("Ingrese la relacion de los nodo/vertices 0 para terminar: ")
    i=int(input("Nodo i: "))
    j=int(input("Nodo j: "))
    while i!=0 and j!=0:
        ungrafo.relacion(i,j)
        i=int(input("Nodo i: "))
        j=int(input("Nodo j: "))
        
    ungrafo.mostrar()
    #N=int(input("Ingrese el nodo que desea comprobar su adyacencia"))
    #ungrafo.adyacentes(N)
    print("Ingrese los nodos para ver el camino (i)")
    i=int(input("Nodo i: "))
    j=int(input("Nodo j: "))
    ungrafo.camino(i,j)
    
    print("Grafo conexo ",ungrafo.conexo())
    ungrafo.aciclico()
