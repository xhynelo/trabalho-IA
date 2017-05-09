from pyparsing import line

n = 4
lines = [[False]*(n-1) for _ in range(n)]
columns = [[False]*(n-1) for _ in range(n)]

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
        if not lines[mat][pos]:
            lines[mat][pos] = True
            return True
        else:
            return False
    else:
        return False

def score(cur_move):
    cur_move = cur_move.split(" ")
    x = int(cur_move[1])
    y = int(cur_move[2])
    if cur_move == "l":
        if not columns[y][x]:
            return False
        if not x == 0:
            if not lines[x-1][y] and not columns[y][x-1]:
                return False
            if not y == n-1:
                if not columns[y+1][x-1]:
                    return False
        if not x == n:
            if not lines[x+1][y]:
                return False
        if not y == n-1:
            if not columns[y+1][x]:
                return False
def ponto_cima(matriz, x, y):
    if not matriz[x-1][y]:
        return False



def score2(cur_move):
    cur_move = cur_move.split(" ")
    x = int(cur_move[1])
    y = int(cur_move[2])

    if cur_move == "l":
        ponnto_cima(x, y)
        if not columns[y][x]:
            return False
        if not x == 0:
            if not lines[x - 1][y] and not columns[y][x - 1]:
                return False
            if not y == n - 1:
                if not columns[y + 1][x - 1]:
                    return False
        if not x == n:
            if not lines[x + 1][y]:
                return False
        if not y == n - 1:
            if not columns[y + 1][x]:
                return False


    elif cur_move == "c":
        if not lines[y][x]:
            return False
        if not x == 0:
            if not columns[x-1][y] and not lines[y][x-1]:
                return False
            if not y == n-1:
                if not lines[y+1][x-1]:
                    return False
        if not x == n:
            if not columns[x+1][y]
                return False
        if not y == n-1:
            if not lines[y+1][x]:
                return False
        
    return True

def