n = int(input())
num = list(map(int, input().split()))
operator = list(map(int, input().split()))
r = []

def ooo(a, b):
    if a == n-1:
        r.append(b)
        return
    for i in range(4):
        if operator[i] > 0:
            operator[i] -= 1
            if i == 0:
                ooo(a+1, b+num[a+1])
            elif i == 1:
                ooo(a+1, b-num[a+1])
            elif i == 2:
                ooo(a+1, b*num[a+1])
            elif i == 3:
                if b < 0:
                    ooo(a+1, (abs(b)//num[a+1])*-1)
                else:
                    ooo(a+1, b//num[a+1])
            operator[i] += 1

ooo(0, num[0])
print(max(r))
print(min(r))