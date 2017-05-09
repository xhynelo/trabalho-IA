from __future__ import print_function
from pyparsing import line

n = 4
lines = [[False]*(n-1) for _ in range(n)]
columns = [[False]*(n-1) for _ in range(n)]

class Player:
    def pontuacao(self, pontuacao):
        self.pontuacao = pontuacao

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


def score(cur_move):
    cur_move = cur_move.split(" ")
    x = int(cur_move[1])
    y = int(cur_move[2])
    ponto = 0
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
    if orientacao == "l":
        x = input("Insira em qual linha que você quer por: (0~"+str(n-1)+")")
        y = input("Insira qual posição da linha você quer por: (0~"+str(n-2)+")")
    if orientacao == "c":
        x = input("Insira em qual coluna que você quer por: (0~"+str(n-1)+")")
        y = input("Insira qual posição da coluna você quer por: (0~"+str(n-2)+")")

    return str(orientacao+" "+x+" "+y)

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
            move(s)
            stemp = score(s)
            turno.pontuacao = stemp
            if stemp == 0:
                turno = ia
        if turno == ia:
            printa_matriz()
            print("IA")
            s=entrada()
            move(s)
            stemp = score(s)
            turno.pontuacao = stemp
            if stemp == 0:
                turno = humano
    print("Score humano: ", humano.pontuacao)
    print("Score ia: ", ia.pontuacao)

main()