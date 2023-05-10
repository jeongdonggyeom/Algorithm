n = int(input())
b = [0] * n
cnt = 0

def check(a):
    for i in range(a):
        if b[a] == b[i] or abs(b[a] - b[i]) == abs(a-i):
            return False
    return True

def qqq(a):
    global cnt
    if a == n:
        cnt += 1
        return
    
    for i in range(n):
        b[a] = i
        if check(a):
            qqq(a+1)

qqq(0)
print(cnt)