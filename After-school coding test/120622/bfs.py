import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())
array = [[0 for col in range(N+1)] for row in range(N+1)]
dist = [0 for i in range(N+1)]
vs = [False] * (N+1)

def bfs(g, v, vs, dist):
    q = deque([v])
    dist[v] = 0
    while q:
        v = q.popleft()
        for i in range(len(g[v])):
            if not vs[i] and g[v][i] == 1:
                q.append(i)
                if dist[i] == 0:
                    dist[i] = dist[v]+1


for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    array[a][b] = 1

bfs(array, X, vs, dist)
if K in dist:
    for i in dist:
        if i == K:
            print(dist.index(i))
            dist[dist.index(i)] = 0
else: print('-1')