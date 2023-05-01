def dfs(v):
    d_v[v] = True
    print(v, end=' ')

    for i in range(1, n+1):
        if d_v[i] == 0 and graph[v][i] == 1:
            dfs(i)

from collections import deque

def bfs(start):
    q = deque([start])

    b_v[start] = True

    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if not b_v[i] == 1 and graph[v][i] == 1:
                q.append(i)
                b_v[i] = True


n, m, v = map(int, input().split())
d_v = [0] * (n+1)
b_v = [0] * (n+1)
graph = [[0] * (n+1) for i in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

dfs(v)
print()
bfs(v)