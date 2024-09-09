from ListaSecPP import ListaSec
if __name__ =="__main__":
    lis=ListaSec(10)
    lis.Insertar(10)
    lis.Insertar(5)
    lis.Insertar(7)
    lis.Insertar(5)
    lis.Insertar(2)
    lis.Insertar(10)

    lis.Recorrer()
    lis.elimarDUp()
    lis.Recorrer()