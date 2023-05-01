from collections import deque

n, m = map(int, input().split())
li = [list(map(int,input())) for i in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=m or li[nx][ny]==0: 
                continue
            
            if li[nx][ny] == 1:
                li[nx][ny] = li[x][y] + 1
                q.append((nx, ny))
    return li[n-1][m-1]

print(bfs(0, 0))