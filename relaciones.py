parejas = []


def createUniverse(parejas):
    '''Crea el universe de todos los elementos de las parejas
        Recibe como parametro las parejas ordenadas
        Devuelve un arreglo unidimensional
    '''
    universe = []
    for p in parejas: 
        if p[0] not in universe:
            universe.append(p[0])
        if p[1] not in universe:
            universe.append(p[1])
    return universe

def createBinaryMatrix(universe, parejas):
    '''Llena la matriz binaria con uno cuando se encuentra el elemento
        Recibe como parametro todas las parejas ordenadas dadas y el universo de elementos
        Devuelve una matriz binaria
    '''
    binaryMatrix = [[0 for x in range(0,len(universe))] for y in range(0,len(universe))] 
    for p in parejas:
        i = universe.index(p[0])
        j = universe.index(p[1])
        binaryMatrix[i][j] = 1
    return binaryMatrix


def isReflexive(binaryMatrix):
    reflexive = True
    for i in range (0, len(binaryMatrix[0])):
        if binaryMatrix[i][i] == 0:
            reflexive = False
    return reflexive









for i in range(0, 3):
    pareja = input("Inserta las parejas ordenadas a,b o no introduzcas nada para terminar\n")
    parejas.append(pareja)

# print(parejas)
# print(createUniverse(parejas))
# print(createBinaryMatrix(createUniverse(parejas), parejas))
matrix = createBinaryMatrix(createUniverse(parejas), parejas)
reflexive = isReflexive(matrix)
print("es reflexiva: " + str(reflexive))