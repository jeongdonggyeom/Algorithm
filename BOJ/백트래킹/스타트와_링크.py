import sys
input = sys.stdin.readline

n = int(input().rstrip())
li = [list(map(int, input().rstrip().split())) for _ in range(n)]
v = [0] * n
mi = 124190412

def ihatecodingtest(idx, a):
    global mi
    if a == n//2:
        power_start = 0
        power_link = 0
        for i in range(n):
            for j in range(i, n):
                if v[i] and v[j]:
                    power_start += li[i][j] + li[j][i]
                elif not v[i] and not v[j]:
                    power_link += li[i][j] + li[j][i]
        mi = min(mi, abs(power_start - power_link))    
        return
    
    for i in range(idx, n):
        if v[i] == 0:
            v[i] = 1
            ihatecodingtest(i+1, a+1)
            v[i] = 0

ihatecodingtest(0, 0)
print(mi)