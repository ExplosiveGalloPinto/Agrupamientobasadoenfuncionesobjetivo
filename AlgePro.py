import matplotlib.pyplot as plt

#Variables Globales
#puntos en formato [xpos,ypos,color]
puntos = []
puntosBU=[]
grupos = []
valorQ = 0
valorQtemp = 0
MatU = []
colorPuntos = ['bo', 'go', 'ro', 'co', 'mo', 'yo', 'ko', 'wo']
colorGrupos = ['b^', 'g^', 'r^', 'c^', 'm^', 'y^', 'k^', 'w^']
centroidesX = []
centroidesY = []

#Variables globales provicionales
tProv = 80
def validarPunto(punto,lista):
    if punto==[]: #Valida si el punto es vacio
        return False
    elif punto in lista: #Valida si el punto ya se encuentra en la lista
        return False
    else:
        return True

def insertarPunto(xpos, ypos, color):
    global puntos #necesario para modificar la variable global
    nuevoPunto = [[xpos,ypos,color]]
    if validarPunto(nuevoPunto,puntos):
        puntos += nuevoPunto
    else:
        print("Error: el punto ya existe")
        
def randomizer(rangoIni, rangoFin):
    from random import randint
    randomValue=randint(rangoIni,rangoFin)
    return randomValue

def crearPunto():
    global tProv
    #Valores randomizados para crear puntos
    xpos = randomizer(1,tProv)
    ypos = randomizer(1,tProv)
    color = 'ko'
    insertarPunto(xpos,ypos,color)

def crearPuntos(nPuntos):
    while nPuntos>0:
        crearPunto()
        nPuntos-=1

def modificarColorPunto(punto,color):
    if punto==[]:
        print("Error: No se puede modificar un punto que no existe")
    elif punto in puntos:
        posPunto=puntos.index(punto)
        puntos[posPunto][2] = color
    else:
        print("Error: No se puede modificar un punto que no existe")
        
def seleccionarGrupos(nGrupos):
    global grupos,puntos
    grupos = []
    while nGrupos>0:
        indice = randomizer(0,len(puntos)-1)
        if validarPunto(puntos[indice],grupos):
            modificarColorPunto(puntos[indice],colorGrupos[nGrupos])
            grupos += [puntos[indice]]
            nGrupos-=1

def calcularDistancia(grupo, punto):
    grupo = grupo[:-1]
    punto = punto[:-1]
    from scipy.spatial import distance
    dis = distance.euclidean(grupo,punto)
    return dis

def test(N,K):
    crearPuntos(N)
    seleccionarGrupos(K)
    pintaPuntos()

def iterador():
    global centroidesX, centroidesY
    centroidesX = []
    centroidesY = []
    calcularMatrizU()
    agrupador()
    calcularMedia(0)
    calcularMedia(1)
    pintaPuntos()
    actualizarCentroide()
    print("Q previo: ", valorQtemp)
    print("Q actual: ", valorQ)

    

def calcularMatrizU():
    temp = []
    temp2 = []
    global puntos, grupos, MatU, valorQ, valorQtemp
    MatU = []
    valorQtemp = valorQ
    valorQ = 0
    for i in puntos:
        temp = []
        temp2 = []
        for j in grupos:
            dist=calcularDistancia(j,i)
            temp += [dist]
            temp2 += [[j,i,dist]]
        indice=temp.index(min(temp))
        valorQ += min(temp)
        MatU+= [temp2[indice]]
        
    
def agrupador():
    global MatU, puntos
    for i in MatU:
        if i[1] in grupos:
            modificarColorPunto(i[1],i[0][2])
        else:
            modificarColorPunto(i[1],i[0][2].replace('^','o'))

def calcularMedia(indice):
    global MatU, grupos, centroidesX,centroidesY
    temp = []
    for i in grupos:
        temp = []
        for j in MatU:
            if i == j[0]:
                temp += [j[1][indice]] #indice 0 para x y 1 para y
        print(temp)        
        if indice == 0:
            centroidesX+=[float(sum(temp)) / max(len(temp), 1)]
        else:
            centroidesY+=[float(sum(temp)) / max(len(temp), 1)]

def actualizarCentroide():
    global grupos,puntos,centroidesX,centroidesY
    for i in grupos:
        for j in puntos:
            if i == j:
                i[0] = centroidesX[grupos.index(i)]
                i[1] = centroidesY[grupos.index(i)]
                j[0] = centroidesX[grupos.index(i)]
                j[1] = centroidesY[grupos.index(i)]

def limpiarLista(lista): #CLEAN TALVEZ INNECESARIO
    cleanlist=[]
    for i in lista:
        if i not in cleanlist:
            cleanlist.append(i)
    return cleanlist    
    
##UIX
    
def pintaPuntos():
    global puntos
    for i in puntos:
        plt.plot(i[0],i[1],i[2])
    plt.axis([0, 100, 0, 100])
    plt.show()
