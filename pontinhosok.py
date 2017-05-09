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
    ponto = 0;

    if cur_move == "l":
        if not x == 0 and not y == n-1:
            if lines[x-1][y] and columns[y][x-1] and columns[y+1][x-1]:
                ponto+=1
        if not x == n and not y == n-1:
            if lines[x+1][y] and columns[y][x] and columns[y+1][x]:
                ponto+=1

    elif cur_move == "c":
        if not x==0 and not y==n-1:
            if not x == 0 and not y == n - 1:
                if columns[x - 1][y] and lines[y][x - 1] and lines[y + 1][x - 1]:
                    ponto += 1
            if not x == n and not y == n - 1:
                if columns[x + 1][y] and lines[y][x] and lines[y + 1][x]:
                    ponto += 1

    return ponto

def printa_matriz()
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
	    print("  ",i, end="")
