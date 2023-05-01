from collections import deque

m, n = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]
q = deque()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cnt = 0
max = 0
flag = False

for i in li:
    cnt += i.count(0)

if cnt == 0:
    print(cnt)

else:
    for i in range(len(li)):
        for j in range(len(li[i])):
            if li[i][j] == 1:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        if li[x][y] != 0:
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue

                if li[nx][ny] == 0:
                    li[nx][ny] = li[x][y] + 1
                    q.append((nx, ny))
    
    for i in li:
        for j in i:
            if j == 0:
                flag = True
            elif j > max:
                max = j
    
    if flag:
        print(-1)
    else:
        print(max-1)