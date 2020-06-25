def mapa():
    return [x.split(" ") for x in open("prueba.txt").readlines()]

"""
# lista de listas sin el \n
def nuevomapa():
    return [[x.replace('\n','') for x in caminos] for caminos in mapa()]
"""

#busca la posicion de x en la matriz
def buscar_en_matriz(matriz,cont):
    if matriz == []:
        return (-1,-1)
    if "X" in matriz[0]: 
        return (cont,matriz[0].index("X"))
    return buscar_en_matriz(matriz[1:],cont+1)
#Ejemplo de movimiento

