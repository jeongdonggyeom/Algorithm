import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
li = [list(map(lambda x: ord(x)-65, input().rstrip())) for _ in range(n)]
visited = [0] * 26
cnt = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, a):
    global cnt
    cnt = max(a, cnt)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and visited[li[nx][ny]] == 0:
            visited[li[nx][ny]] = 1
            dfs(nx, ny, a+1)
            visited[li[nx][ny]] = 0

    return cnt

visited[li[0][0]] = 1
print(dfs(0, 0, 1))