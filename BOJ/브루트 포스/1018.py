n, m = map(int, input().split())
li = [input() for _ in range(n)]
cnt = []

for i in range(n-7): # 8x8 판이 index가 넘어가지 않도록 -7
    for j in range(m-7):
        drawB = 0
        drawW = 0

        for a in range(i, i+8): # 8x8 검사
            for b in range(j, j+8):
                if (a+b)%2==0: # 나머지가 0일땐 검은색이 아닐 때 검은색 +1, 나머지가 1일 땐 검은색일 때 검은색 +1을 하여
                               # 시작점이 검, 흰 2가지 경우를 해결함 
                    if li[a][b] != 'B':
                        drawB+=1
                    elif li[a][b] != 'W':
                        drawW += 1
                else:
                    if li[a][b] != 'W':
                        drawB += 1
                    elif li[a][b] != 'B':
                        drawW += 1
        cnt.append(drawB)
        cnt.append(drawW)
    
print(min(cnt))