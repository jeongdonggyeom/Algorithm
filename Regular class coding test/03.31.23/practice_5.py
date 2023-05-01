n = int(input())
li = [list(map(int,input().split())) for _ in range(n)]
visited = [False for _ in range(n)]
cnt = 0

def dfs(n, li, i, visited):
    visited[i] = True
    for j in range(n):
        if j != i and li[i][j] == 1:
            if visited[j] == False:
                dfs(n, li, j, visited)

for i in range(n):
    if visited[i] == False:
        dfs(n, li, i, visited)
        cnt += 1

print(cnt)