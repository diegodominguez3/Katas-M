def vecinos(game):
    global celcolumn
    global celline
    global column
    global line
    vecino = 0
    if celcolumn == 0:
        if celline == 0:
            if game[celcolumn][celline+1] == "*":
                vecino += 1
            if game[celcolumn+1][celline] == "*":
                vecino += 1
            if game[celcolumn+1][celline+1] == "*":
                vecino += 1
        elif celline == (line-1):
            if game[celcolumn][celline-1] == "*":
                vecino += 1
            if game[celcolumn-1][celline] == "*":
                vecino += 1
            if game[celcolumn-1][celline-1] == "*":
                vecino += 1
        else:
            if game[celcolumn][celline-1] == "*":
                vecino += 1
            if game[celcolumn][celline+1] == "*":
                vecino += 1
            for line2 in range(-1,2):
                if game[celcolumn+1][celline+line2] == "*":
                    vecino += 1
    elif celcolumn == (column-1):
        if celline == 0:
            if game[celcolumn][celline+1] == "*":
                vecino += 1
            if game[celcolumn-1][celline] == "*":
                vecino += 1
            if game[celcolumn-1][celline+1] == "*":
                vecino += 1
        elif celline == (line-1):
            if game[celcolumn-1][celline] == "*":
                vecino += 1
            if game[celcolumn-1][celline-1] == "*":
                vecino += 1
            if game[celcolumn][celline-1] == "*":
                vecino += 1
        else:
            if game[celcolumn][celline-1] == "*":
                vecino += 1
            if game[celcolumn][celline+1] == "*":
                vecino += 1
            for line3 in range(-1,2):
                if game[celcolumn-1][celline+line3] == "*":
                    vecino += 1
    else:
        if celline == 0:
            for line4 in range(0,2):
                if game[celcolumn-1][celline+line4] == "*":
                    vecino += 1
            for line5 in range(0,2):
                if game[celcolumn+1][celline+line5] == "*":
                    vecino += 1
            if game[celcolumn][celline+1] == "*":
                vecino += 1                
        elif celline == (line-1):
            for line6 in range(-1,1):
                if game[celcolumn-1][celline+line6] == "*":
                    vecino += 1
            for line7 in range(-1,1):
                if game[celcolumn+1][celline+line7] == "*":
                    vecino += 1
            if game[celcolumn][celline-1] == "*":
                vecino += 1
        else:
            for line8 in range(-1,2):
                if game[celcolumn-1][celline+line8] == "*":
                    vecino += 1
            for line8 in range(-1,2):
                if game[celcolumn+1][celline+line8] == "*":
                    vecino += 1
            if game[celcolumn][celline-1] == "*":
                vecino += 1
            if game[celcolumn][celline+1] == "*":
                vecino += 1
    return vecino

def NextOfspring(u):
    """
        Esta funcion recibe un universo y regresa la siguiente generacion segun las reglas
        Nota: La funcion recibe la cadena el el formato establecido y lo regresa en el mismo formato
    """
    global column
    global line
    global celcolumn
    global celline
    
    u2 = GetUniverse(u)
    sep = u2.split("\n")
    del sep[-1]
    cp = u2.split("\n")
    del cp[-1]
    celcolumn = -1
    for linea in sep:
        celline = 0
        celcolumn += 1
        cp[celcolumn] = ""
        for cell in linea:
            r = vecinos(sep)
            if r == 3 and cell == ".":
                cp[celcolumn] += "*"
            elif (r == 1 or r == 0) and cell == "*":
                cp[celcolumn] += "."
            elif (r == 2 or r == 3) and cell == "*":
                cp[celcolumn] += "*"
            elif r > 3 and cell == "*":
                cp[celcolumn] += "."
            else:
                cp[celcolumn] += "."
            celline += 1
    fin = ""
    for i in cp:
        fin += i
    return (str(column)+str(line)+fin)
    
    raise NotImplementedError

def GetUniverse(u):
    """
        Esta funcion debe de regresar el universo en el formato establecido 
        pero regresa el universo sin el renglon de las dimenciones y con los saltos
        de linea correspondientes
    """
    global line
    global column
    if u[0:2].isdigit() == True:
        line = int(u[1])
        column = int(u[0])
    u2 = ""
    for line2 in range(0,column):
        u2 += u[(line2*line)+2:(line2*line)+2+line] + "\n"
    u = u2
    return u
    
    raise NotImplementedError

line = 0
column = 0
celline = 0
celcolumn = 0

if __name__ == '__main__':
    print("Captura un universo (Linea por linea segun el formato y vacio para terminar)")
    u = ""
    line = input()
    while(line != ""):
        u += line
        line = input()
    option = input("Teclee n para ver la siguiente generacion y s para deter la simulacion")
    while(option == "n"):
        u = NextOfspring(u)
        print(GetUniverse(u))
        option = input()
        
