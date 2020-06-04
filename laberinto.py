def mapa():
    return [x.split(" ") for x in open("prueba.txt").readlines()]

def inicio(mapa):
    print(mapa[:1])
    if 'x' in mapa[0] :
        return("estas en la pos inicio")
    elif 'x' in mapa[:1]:
        print(mapa[0])
        return ("fuck")
        
#def recorrido(mapa):
print(inicio(mapa()))
