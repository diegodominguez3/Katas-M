# coding: utf8
board= ["1","2","3","4","5","6","7","8","9"]
template = " {} │ {} │ {} \n───┼───┼───\n {} │ {} │ {} \n───┼───┼───\n {} │ {} │ {} "
template2 = " {} │ {} │ {} \n───┼───┼───\n {} │ {} │ {} \n───┼───┼───\n {} │ {} │ {} "
ganador = ""
turno = 0
def GetTablero():
    global tempalte
    global board
    return template2.format(board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8])
    
    """
        Esta funcion debe regresar el tablero en forma de cadena
        Nota: Usar el template de arriba
    """
    raise NotImplementedError
def JuegoContinua():
    global ganador
    if board[0] == "X" and board[1] == "X" and board[2] == "X":
        ganador = "X"
        return False
    if board[3] == "X" and board[4] == "X" and board[5] == "X":
        ganador = "X"
        return False
    if board[6] == "X" and board[7] == "X" and board[8] == "X":
        ganador = "X"
        return False
    if board[0] == "X" and board[3] == "X" and board[6] == "X":
        ganador = "X"
        return False
    if board[1] == "X" and board[4] == "X" and board[7] == "X":
        ganador = "X"
        return False
    if board[2] == "X" and board[5] == "X" and board[8] == "X":
        ganador = "X"
        return False
    if board[0] == "X" and board[4] == "X" and board[8] == "X":
        ganador = "X"
        return False
    if board[2] == "X" and board[4] == "X" and board[6] == "X":
        ganador = "X"
        return False
    if board[0] == "O" and board[1] == "O" and board[2] == "O":
        ganador = "O"
        return False
    if board[3] == "O" and board[4] == "O" and board[5] == "O":
        ganador = "O"
        return False
    if board[6] == "O" and board[7] == "O" and board[8] == "O":
        ganador = "O"
        return False
    if board[0] == "O" and board[3] == "O" and board[6] == "O":
        ganador = "O"
        return False
    if board[1] == "O" and board[4] == "O" and board[7] == "O":
        ganador = "O"
        return False
    if board[2] == "O" and board[5] == "O" and board[8] == "O":
        ganador = "O"
        return False
    if board[0] == "O" and board[4] == "O" and board[8] == "O":
        ganador = "O"
        return False
    if board[2] == "O" and board[4] == "O" and board[6] == "O":
        ganador = "O"
        return False
    else:
        return True
    """
        Debe de regresar verdadero si el juego continua o false si ha terminado
    """
    raise NotImplementedError
    
def IntentarTirada(casilla):
    global turno
    global template
    global ganador
    global board
    if int(casilla) > 9 or int(casilla) < 1:
        return "La tirada debe de estar entre 1 y 9"
    if template.find((board[(casilla)-1])) == -1:
        return "La casilla ya esta ocupada"
    else:
        if turno % 2 == 0:
            board[((casilla)-1)] = "X"
            turno += 1
            JuegoContinua()
            if ganador == "X":
                return "Felicidades X as ganado. weeee"
        elif turno % 2 == 1:
            board[(casilla)-1] = "O"
            turno += 1
            JuegoContinua()
            if ganador == "O":
                return "Felicidades O as ganado. weeee"
        if turno == 9:
            return "Juego empatado. :("
        return ""
                        
    raise NotImplementedError               
    
    """
        Esta funcion recibe el intento del jugador por ocupar una casilla
        y regresa una cadena segun los siguientes criterios:
        Si esta fuera de rango: "La tirada debe de estar entre 1 y 9"
        Si la casilla esta ocupada: "La casilla ya esta ocupada"
        Si x a ganado: "Felicidades X as ganado. weeee"
        Si o a ganado: "Felicidades O as ganado. weeee"
        Si el juego a quedado empatado: "Juego empatado. :("
        Ninguna de las anteriores: "" (cadena vacia)
    """
   
def IniciaJuego():
    global template
    global turno
    global ganador
    template = " {} │ {} │ {} \n───┼───┼───\n {} │ {} │ {} \n───┼───┼───\n {} │ {} │ {} ".format(board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8])
    turno = 0
    ganador = ""
    """
        Esta function se puede utilizar para re iniciar variables.
        Si no se usa se puede dejar vacia
    """
    return None

if __name__ == '__main__':
    IniciaJuego() 
    while(JuegoContinua()):
        print(GetTablero())
        msg = ""
        casilla = int(input("Escoge una casilla: "))
        msg = IntentarTirada(casilla)
        IntentarTirada(casilla)
        if msg != "":
            print(msg)
