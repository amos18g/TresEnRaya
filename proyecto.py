
#// Esta variable de tipo booleano servira como bandera para decidir el turno de cada jugador
turnoDeX = False

#Variable que reunira las condiciones para finalizar el program
condicion = True

#Lista de tipo caracter la cual simulara el tablero de juego
tablero = [['_','_','_'],
           ['_','_','_'],
           ['_','_','_']
            ]



    
#Esta funcion sirve para determinar si hay un campeon haciendo uso de
# de ciclos while y condicionales if 
    

def hayGanador():
    #variable poscicional

    i = 0
    #Validacion horizontal: Comprueba si una linea en horizonal de la matriz esta contiene el mismo caracter X o 0, en caso de ser alguno de estos caracteres
    #lo retorna
    while(i<3):        
        if(tablero[i][0] != '_' and tablero[i][0] == tablero[i][1] and tablero[i][1] == tablero[i][2]):
            return tablero[i][0]
        i = i + 1

    #Refrescando la variable posicional
    i = 0

    #Validacion vertical: Comprueba si una linea en vertical de la matriz esta contiene el mismo caracter X o 0 en caso de ser alguno de estos caracteres
    #lo retorna
    
    while(i<3):
        if(tablero[0][i] != '_' and tablero[0][i] == tablero[1][i] and tablero[1][i] == tablero[2][i]):
            return tablero[0][i]
        i = i + 1

    #Validacion Diagonal de izquierda a derecha: comprueba si la diagonal diagonal de la matriz tienne el mismo caracter X o 0 en caso de ser alguno de estos caracteres
    #lo retorna
        
    if(tablero[0][0] != '_' and tablero[0][0] == tablero[1][1] and tablero[1][1] == tablero[2][2]):
        return tablero[0][0]

    #Validacion Diagonal de Derecha a Izquierda comprueba si la diagonal diagonal de la matriz tienne el mismo caracter X o 0 en caso de ser alguno de estos caracteres
    #lo retorna
    
    if(tablero[0][2] != '_' and tablero[0][2] == tablero[1][1] and tablero[1][1] == tablero[2][0]):
        return tablero[0][2]

  

        
# esta funcion hace uso de ciclos de repeticion while y condicionales para comprobar si se dio un empate en el juego
# esto lo hace comprobando si cada una de las pociones en la matriz son distintas de el caracter "_" retornando verdadero en dicho caso


def hayEmpate():
    i = 0
    j = 0

    while(i<3):            
        while(j<3):
            if(tablero[i][j] == '_'):
                return False
            j = j + 1
        j = 0
        i = i + 1
        
    return True



# Esta funcion se encargar de mostrar el tablero vacion y en cada movimiento del juego
# ademas llama a las funciones necesarias para determinar si algun jugador gano la partida o si se da un empena
# finalmente intercambia el valor de la variable encargada de cambiar el turno de cada jugador
    
def mostrarTablero():

    # se declara que se usaran las variables globales turnoDeX y condicion para poder usarlas dentro de la funcion  
    global turnoDeX
    global condicion

    #Esta condicional con ayuda de la variable  booleana turnoDeX determina el turno del jugador
    #y le asigna el caracter X o 0 a la variable jugador
    
    if turnoDeX == True:
        jugador = 'X'
    else:
        jugador = '0'
    
    #el clico for se encarga de mostrar el tablero almacenado en la lista tablero
    
    for i in tablero:
        print(i)

    print(" ")

    #se pregunta la posicion en la que se desea jugar y se asigna la variable jugador
    #   a la matriz en dicha posicion
    
    print("Es el turno de ",jugador)
    fila = int(input("En que fila desea jugar: "))
    
    columna = int(input("En que columna desea jugar: "))
    
    tablero[fila][columna] = jugador

    # se llama a la funcion hayGanador para determinar si un jugador gano y si es X o Y y uno de estos caracteres se le asignan
    # a la variable ganador

    ganador = hayGanador()

    # Con ayuda de las funciones hayGanador y hayEmpate se determina si algun jugador gano
    #o si se dio empate, independientemente del caso se le asigna el valor de falso a la variable
    # condicion, esto detendra el ciclo while en funcion principal

    if(ganador == 'X' or ganador == '0'):
        print(' Has ganado ', ganador)
        condicion = False

    elif(hayEmpate() == True):
        print( 'Hay empate \n' )
        condicion = False

    # se cambia el valor de la variable global turnoDeX a su opuesto booleano
    
    turnoDeX = not turnoDeX


   
    


if __name__ == '__main__':

    # con ayuda de  un clico while se llamara a la funcion mostrat tablero hasta que se encuentre un ganador o empate, en dicho caso
    # la variable condicion sera falsa
    
    while(condicion == True):
        mostrarTablero()
   




