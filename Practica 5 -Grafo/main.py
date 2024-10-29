from grafoSecu import grafo
if __name__=='__main__':
    ver=int(input("Ingrese cantidad de vertices: "))
#    d=input("Es una matriz de pesos V/F\n")
#    while d.upper()!='V' and d.upper()!='F':
#        print("Opcion invalida\n")
#        d=input("Es unamatriz de pesos- V/F\n")
#    if d.upper()=='V':
#        d=True
#    else:
#        d=False
    ungrafo=grafo(ver)

    print("Ingrese la relacion de los nodo/vertices 0 para terminar: ")
    i=int(input("Nodo i: "))
    j=int(input("Nodo j: "))
    while i!=0 and j!=0:
 #       if d==True:
#            p=int("INgrese el peso")
#            ungrafo.pesos(i,j,p)
#        else:
        ungrafo.relacion(i,j)
        i=int(input("Nodo i: "))
        j=int(input("Nodo j: "))
        
    ungrafo.mostrar()
    ungrafo.BEA(1)
    ungrafo.BEP()
    N=int(input("Ingrese el nodo que desea comprobar su adyacencia"))
    ungrafo.adyacentes(N)
    print("Ingrese los nodos para ver el camino (i)")
    i=int(input("Nodo i: "))
    j=int(input("Nodo j: "))
    ungrafo.camino(i,j)
    
    print("Grafo conexo ",ungrafo.conexo())
    ungrafo.aciclico()
