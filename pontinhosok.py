n = 4
lines = [[False]*(n-1) for _ in range(n)]
columns = [[False]*(n-1) for _ in range(n)]

class Player:
    pontos=0
    def pontuacao(self, pontos):
        self.pontos = pontos

    

def move(smove):
    smove = smove.split(" ")
    mat = int(smove[1])
    pos = int(smove[2])
    if smove[0] == "l":
        if not lines[mat][pos]:
            lines[mat][pos] = True
            return True
        else:
            return False
    elif smove[0] == 'c' :
        if not columns[mat][pos]:
            columns[mat][pos] = True
            return True
        else:
            return False
    else:
        return False


def undo_move(smove):
    smove = smove.split(" ")
    mat = int(smove[1])
    pos = int(smove[2])
    if smove[0] == "l":
        lines[mat][pos] = False
    elif smove[0] == 'c':
        columns[mat][pos] = False

def score(cur_move):
    cur_move = cur_move.split(" ")
    x = int(cur_move[1])
    y = int(cur_move[2])
    ponto = 0
    if cur_move[0] == "l":
        try:
            if not x == 0:
                if lines[x-1][y] and columns[y][x-1] and columns[y+1][x-1]:
                    ponto+=1
        except:
            ...
        try:
            if lines[x+1][y] and columns[y][x] and columns[y+1][x]:
                ponto+=1
        except:
            ...
    elif cur_move[0] == "c":
        try:
            if not x == 0:
                if columns[x - 1][y] and lines[y][x - 1] and lines[y + 1][x - 1]:
                    ponto += 1
        except:
            ...
        try:
            if columns[x + 1][y] and lines[y][x] and lines[y + 1][x]:
                ponto += 1
        except:
            ...
    return ponto


def printa_matriz():
    print(" ", end="")
    for x in range(len(lines)):
        print(x, "  ", end="")
    print("")
    for i, linha in enumerate(lines):
        print(i, end="")
        for x in linha:
            print("*", end="")
            print("---" if x else "   ", end="")
        print("*")
        if i == len(columns[-1]):
            break
        print(" ", end="")
        for x in columns:
            print("|   " if x[i] else "    ", end="")
        print(i)
    for i in range(len(lines)-1):
        print("  ", i, end="")
    print("\n")

def entrada():
    orientacao = input("Quer fazer uma Linha ou Coluna? (l/c)")
    while orientacao != "l" and orientacao != "c":
        orientacao = input("(l/c)")
    if orientacao == "l":
        x = input("Insira em qual linha que você quer por: (0~"+str(n-1)+")")
        while x > str(n-1) or int(x) < 0:
            x = input("(0~" + str(n - 1) + ")")
        y = input("Insira qual posição da linha você quer por: (0~"+str(n-2)+")")
        while y > str(n-2) or int(y) < 0:
            y = input("(0~" + str(n - 2) + ")")
    if orientacao == "c":
        x = input("Insira em qual coluna que você quer por: (0~"+str(n-1)+")")
        while x > str(n-1) or int(x) < 0:
            x = input("(0~" + str(n - 1) + ")")
        y = input("Insira qual posição da coluna você quer por: (0~"+str(n-2)+")")
        while y > str(n-2) or int(y) < 0:
            y = input("(0~" + str(n - 2) + ")")
    return f"{orientacao} {x} {y}"


def fimDeJogo():
    for i in range(n):
        for j in range(n-1):
            if not lines[i][j]:
                return False
    for i in range(n):
        for j in range(n - 1):
            if not columns[i][j]:
                return False
    return True


def find_moves():
    res = ""
    lst = []
    for i in range(n):
        for j in range(n-1):
            if not lines[i][j]:
                res = "l {} {}".format(i, j)
                lst.append(res)
            if not columns[i][j]:
                res = "c {} {}".format(i, j)
                lst.append(res)
    return lst


def minimax(depth, ia, humano, iaTurn, pontosIa, pontosHumano, alpha, beta):
     if depth == 0 or fimDeJogo():
         return pontosIa - pontosHumano, None
     stemp = 0
     if iaTurn:
         v = (-n**2-1, None)
         for current_move in find_moves():
             move(current_move)
             stemp = score(current_move)
             pontosIa += stemp
             if score(current_move) == 0:
                v = max(v, (minimax(depth - 1, ia, humano, False, pontosIa, pontosHumano, alpha, beta)[0], current_move))
             else:
                v = max(v, (minimax(depth - 1, ia, humano, True, pontosIa, pontosHumano, alpha, beta)[0], current_move)) #se fez ponto joga dnovo
             alpha = max(alpha, v)
             undo_move(current_move)
             pontosIa -= stemp
             if beta <= alpha:
                 break
         return v
     else:
         v = (n**2+1, None)
         for current_move in find_moves():
             move(current_move)
             stemp = score(current_move)
             pontosHumano +=stemp
             if score(current_move)==0:
                v = min(v, (minimax(depth - 1, ia, humano, True, pontosIa, pontosHumano, alpha, beta)[0], current_move))
             else:
                v = min(v, (minimax(depth - 1, ia, humano, False, pontosIa, pontosHumano, alpha, beta)[0], current_move)) #se fez ponto joga dnovo
             beta = min(beta, v)
             undo_move(current_move)
             pontosHumano -= stemp
             if beta <= alpha:
                 break
         return v

def main():
    humano = Player()
    ia = Player()
    s=""
    turno = humano
    while not fimDeJogo():
        printa_matriz()
        stemp = 0
        if turno == humano:
            print("Humano")
            s=entrada()
            while not move(s):
                print("Linha já marcada")
                s=entrada()
            move(s)
            stemp = score(s)
            turno.pontos += stemp
            if stemp == 0:
                turno = ia
        if turno == ia:
            s = minimax(6, ia, humano, True, ia.pontos, humano.pontos, (-n ** 2 - 1, None), (n ** 2 + 1, None))
            move(s[1])
            stemp = score(s[1])
            turno.pontos += stemp
            if stemp == 0:
                turno = humano
    printa_matriz()
    print("Score humano: ", humano.pontos)
    print("Score ia: ", ia.pontos)

main()
