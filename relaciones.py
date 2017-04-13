parejas = []


def createUniverse(parejas):
    '''Crea el universe de todos los elementos de las parejas
        Recibe como parametro las parejas ordenadas
        Devuelve un arreglo unidimensional
    '''
    universe = [] #Almacena el conjunto de elementos
    for p in parejas: 
        if p[0] not in universe:
            universe.append(p[0])
        if p[1] not in universe:
            universe.append(p[1])
    print(universe)
    return universe

def createBinaryMatrix(universe, parejas):
    '''Llena la matriz binaria con uno cuando los elementos del universo esan relacionados.
        Recibe como parametro todas las parejas ordenadas dadas y el universo de elementos.
        Devuelve una matriz binaria
    '''
    binaryMatrix = [[0 for x in range(0,len(universe))] for y in range(0,len(universe))] #Inicializa en cero matriz nxn
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

def isSimetric(binaryMatrix):
    simetric = True
    for i in range (0, len(binaryMatrix[0])):
        for j in range (0, len(binaryMatrix[0])):
            if binaryMatrix[i][j] != binaryMatrix[j][i]:
                simetric = False
    return simetric

def isAsimetric(binaryMatrix):
    asimetric = False
    for i in range (0, len(binaryMatrix[0])):
        for j in range (0, len(binaryMatrix[0])):
            if i!= j:
                if binaryMatrix[i][j]== 0 or  binaryMatrix[j][i]== 0:
                    asimetric = True
    return asimetric


 

"""
for i in range(0, 6):
    pareja = input("Inserta las parejas ordenadas a,b o no introduzcas nada para terminar\n")
    parejas.append(pareja)
"""
#parejas = [[1,2],[2,1],[3,1],[1,3],[4,4],[5,5]]
# print(parejas)
# print(createUniverse(parejas))
# print(createBinaryMatrix(createUniverse(parejas), parejas))

#matrix = createBinaryMatrix(createUniverse(parejas), parejas)

def initMatrix(parejas):
    matrix = createBinaryMatrix(createUniverse(parejas), parejas)
    print(parejas)
    for row in matrix:
        print(' '.join(map(str,row)) )
    print("Es reflexiva: " + str(isReflexive(matrix)))
    print("Es simetrica: " + str(isSimetric(matrix)))
    print("Es asimetrica: " + str(isAsimetric(matrix)))
    return {'reflexiva': isReflexive(matrix), 'asimetrica': isAsimetric(matrix), 'simetrica': isSimetric(matrix)}

