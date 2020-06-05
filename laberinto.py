def mapa():
    return [x.split("\n") for x in open("prueba.txt").readlines()]

def buscar_en_matriz(matriz,cont):
    if matriz == []:
        return (-1,-1)
    if "X" in matriz[0]: 
        return (cont,matriz[0].index("X"))
    return buscar_en_matriz(matriz[1:],cont+1)
        
#def recorrido(mapa):
print(buscar_en_matriz(mapa(),5))
print(mapa())
