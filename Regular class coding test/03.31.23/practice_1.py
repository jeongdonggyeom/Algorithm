n, m = map(int, input().split())
li = [list(map(int,input())) for i in range(n)]
cnt = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    if li[x][y] == 0:
        li[x][y] = 1
        for i in range(4):
            dfs(x+dx[i], y+dy[i])
        return True

    return False

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            cnt += 1

print(cnt)