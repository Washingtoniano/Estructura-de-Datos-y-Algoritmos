from arbol import arbol
from menu import menu

if __name__ =="__main__":
    unmenu=menu()
    ar=arbol()
    print("Bienvenido")
    op=input("Ingrese la opcion que desea\n 1-Test\n 2-Test iterativo\n 3-Codigo de hufman\n 0-Salir\n")
    while op != '0':
        unmenu.opcion(op,ar)
        op=input("Ingrese la opcion que desea\n 1-Test\n 2-Test iterativo\n 3-Codigo de hufman\n 0-Salir\n")

# Palabras de pruebe:
# Electroencefalografista (23 letras). 
# Anticonstitucionalidad (22 letras). 
# Esternocleidomastoideo (22 letras). 
# Antinorteamericanismo (21 letras).
# Contrarrevolucionario (21 letras).
# Desoxirribonucleótido (21 letras).
# Electroencefalografía (21 letras).
# Interdisciplinariedad (21 letras ).
# Otorrinolaringólogo (21 letras).
# Electroencefalograma (20 letras).
# Otorrinolaringología (20 letras).
# Electrocardiógrafo (19 letras).
# Electrocardiograma (18 letras). 
# Electrodoméstico (16 letras). 
# Arteriosclerosis (16 letras).