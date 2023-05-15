n = int(input())
li = [0] * (n+1)
cnt1 = 1
cnt2 = 0

def f1(n):
    global cnt1
    if n <= 2:
        return 1
    else:
        cnt1 += 1
        return f1(n-1) + f1(n-2)

def f2(n):
    global cnt2
    li[0] = li[1] = 1
    for i in range(2, n):
        cnt2 += 1
        li[i] = li[i-1] + li[i-2]
    return li[n-1]

f1(n)
f2(n)

print(f'{cnt1} {cnt2}')