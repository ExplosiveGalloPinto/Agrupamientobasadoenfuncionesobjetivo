import matplotlib.pyplot as plt

#Variables Globales
#puntos en formato [xpos,ypos,color]
puntos = []
puntosBU=[]
grupos = []
colorPuntos = ['bo', 'go', 'ro', 'co', 'mo', 'yo', 'ko', 'wo']
colorGrupos = ['b^', 'g^', 'r^', 'c^', 'm^', 'y^', 'k^', 'w^']


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
    print(grupo)
    print(punto)
    from scipy.spatial import distance
    dis = distance.euclidean(grupo,punto)
    print("distancia: ", dis)

def test():
    crearPuntos(5)
    seleccionarGrupos(2)
    print("puntos: ", puntos)
    print("grupos: ", grupos)
    calcularDistancia(grupos[1],puntos[2])
    
##UIX
    
def pintaPuntos():
    global puntos
    for i in puntos:
        plt.plot(i[0],i[1],i[2])
    
    plt.axis([0, 100, 0, 100])
    from matplotlib.widgets import Button
    axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
    bnext = Button(axnext, 'Iterar')
    bnext.on_clicked(test)
    plt.show()
