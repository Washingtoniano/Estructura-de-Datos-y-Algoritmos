#http://programminghistorian.org/es/lecciones/manipular-cadenas-de-caracteres-en-python
#Conultar

def dividir(cla,di):
    return cla%di



def extraccion(cla,di,CC):
    #¿Cantidad de claves // en la dimnsion de la tabla?
    digits=(CC//di)
    cla=str(cla)
    cla=cla[digits:]
    return int(cla)%di


def cuadradoM(cla,di,CC):
    #¿Cantidad de claves // en la dimnsion de la tabla, luego divdirelo en 2 para obtener los digitos a elimar desde el inicio y el final?
    # 1000//250=4   4/2=2   Eliminar: 2dig al inicio y 2dig al final 
    cuadrado=str(cla**2)
    medio=len(cuadrado)//2
    cant=(CC//di)/2
    
    cla=(cla[medio-cant:medio+cant])

    return int(cla)%di
def plegado(cla,di,CC):
    lon=(CC//di)
    cla=str(cla)
    total=0
    ne=cla[lon-1:]
    cla=cla-ne
    cla=int(cla)
    total=cla+int(ne)
    return total%di


