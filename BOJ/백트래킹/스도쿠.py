li = [list(map(int, input().split())) for _ in range(9)]
zero = []

for i in range(9):
    for j in range(9):
        if li[i][j] == 0:
            zero.append([i, j])

def w(h, t):
    for i in range(9):
        if li[h][i] == t:
            return False
    return True

def h(w, t):
    for i in range(9):
        if li[i][w] == t:
            return False
    return True

def s(h, w, t):
    x = h//3*3
    y = w//3*3

    for i in range(3):
        for j in range(3):
            if li[x+i][y+j] == t:
                return False
    return True

def sudoku(a):
    if a == len(zero):
        for i in li:
          print(*i)
        return True
    
    x = zero[a][0]
    y = zero[a][1]

    for i in range(1, 10):
        if w(x, i) and h(y, i) and s(x, y, i):
            li[x][y] = i
            if sudoku(a+1):
                return True
            li[x][y] = 0
    return False

sudoku(0)

"""
가로
- 높이 인덱스랑 목표값을 받야아하지

세로
- 가로 인덱스랑 목표값을 받아야지

사각형
- 0의 위치를 받으면 사각형 크기(= 3)만큼 나눠 여기다 3을 곱하면 사각형의 왼쪽 위 점을 알 수 있다

"""