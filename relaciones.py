parejas = []


'''def createUniverse(parejas):
    Crea el universe de todos los elementos de las parejas
        Recibe como parametro las parejas ordenadas
        Devuelve un arreglo unidimensional
    
    universe = [] #Almacena el conjunto de elementos
    for p in parejas: 
        if p[0] not in universe:
            universe.append(p[0])
        if p[1] not in universe:
            universe.append(p[1])
    print(universe)
    return universe
'''
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

def isIrreflexive(binaryMatrix):
    irreflexive = True
    for i in range (0, len(binaryMatrix[0])):
        if binaryMatrix[i][i] == 1:
            irreflexive = False
    return irreflexive

def isSymmetric(binaryMatrix):
    symmetric = True
    for i in range (0, len(binaryMatrix[0])):
        for j in range (0+i, len(binaryMatrix[0])):
            if binaryMatrix[i][j] != binaryMatrix[j][i]:
                symmetric = False
    return symmetric

def isAsimetric(binaryMatrix):
    asimetric = True
    for i in range (0, len(binaryMatrix[0])):
        for j in range (0+i, len(binaryMatrix[0])):
            if binaryMatrix[i][j] == binaryMatrix[j][i]:
                if binaryMatrix[i][j] !=0:
                    asimetric = False
    return asimetric

def isAntisymmetric(binaryMatrix):
    antisimetric = True
    for i in range(0, len(binaryMatrix[0])):
        for j in range(1+i, len(binaryMatrix[0])):
            if binaryMatrix[i][j] == binaryMatrix[j][i]:
                if binaryMatrix[i][j] !=0:
                    antisimetric = False
    return antisimetric

'''
def isTransitive(binaryMatrix):
    transitive = True
    for i in range (0, len(binaryMatrix[0])):
        for j in range (0, len(binaryMatrix[0])):
            if i!=j:
                if(binaryMatrix[i][j]==1):
                    for k in range (0, len(binaryMatrix[0])):
                        if j!=k:
                            if(binaryMatrix[j][k]==1):
                                if(binaryMatrix[i][k]!=1):
                                    transitive = False
    return transitive
'''
def isTransitive(binaryMatrix):
    transitive = True
    for i in range (0, len(binaryMatrix[0])):
        for j in range (0, len(binaryMatrix[0])):
            for k in range (0, len(binaryMatrix[0])):
                if((i!=j) and (j!=k)):
                    if(binaryMatrix[i][j]==1 and binaryMatrix[j][k]==1):
                        if(binaryMatrix[i][k]!=1):
                            transitive = False
    return transitive



            



 

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
    print("Universo o conjunto: " + str(parejas[0]))
    print("Relación:" + str(parejas[1:]))
    matrix = createBinaryMatrix(parejas[0], parejas[1:])
    
    for row in matrix:
        print(' '.join(map(str,row)) )
    print("Es reflexiva: " + str(isReflexive(matrix)))
    print("Es irreflexiva: " + str(isIrreflexive(matrix)))
    print("Es simetrica: " + str(isSymmetric(matrix)))
    print("Es asimetrica: " + str(isAsimetric(matrix)))
    print("Es antisimetrica: " + str(isAntisymmetric(matrix)))
    print("Es transitiva: " + str(isTransitive(matrix)))
    
    
    return {'reflexiva': isReflexive(matrix), 'irreflexiva': isIrreflexive(matrix), 'simetrica': isSymmetric(matrix), 'asimetrica': isAsimetric(matrix), 'antisimetrica': isAntisymmetric(matrix), 'transitiva': isTransitive(matrix), 'parejas':parejas[1:] }

