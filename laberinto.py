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
#hace un movimiento a la derecha siempre y cuando
#aun tenga espacio
def der(mapa,pos):
    return [['0' if i==pos[0] and j== pos[1]
             else 'x' if i== pos[0] and j== pos[1]+1
             else mapa[i][j]  for j in range(len(mapa[i])) ]  for i in range(len(mapa)) ]
def aba(mapa,pos):
    return [['0' if i==pos[0] and j== pos[1]
             else 'x' if i== pos[0]+1 and j== pos[1]
             else mapa[i][j]  for j in range(len(mapa[i])) ]  for i in range(len(mapa)) ]

def izq(mapa,pos):
    return [['0' if i==pos[0] and j== pos[1]
             else 'x' if i== pos[0] and j== pos[1]-1
             else mapa[i][j]  for j in range(len(mapa[i])) ]  for i in range(len(mapa)) ]

def arr(mapa,pos):
    return [['0' if i==pos[0] and j== pos[1]
             else 'x' if i== pos[0]-1 and j== pos[1]
             else mapa[i][j]  for j in range(len(mapa[i])) ]  for i in range(len(mapa)) ]
             
#print(arr(mapa(),buscar_en_matriz(mapa(),0)))

#def solucion(mapa,pos):
    

