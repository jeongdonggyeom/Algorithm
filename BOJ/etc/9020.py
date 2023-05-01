import sys

input = sys.stdin.readline

a = int(input().rstrip())
li = []

for i in range(a):
    b = int(input().rstrip())
    li.append(b)

prime = [1 for _ in range(max(li)+1)]

for i in range(2, max(li)+1):
    for j in range(i*2, max(li)+1, i):
        prime[j] = 0

sosu = set([i for i in range(2, len(prime)) if prime[i]==1])

for i in li:
    li2 = []
    m = 100000
    a, b = 0, 0
    flag = True
    for j in sosu:
        if i%j == 0 and i//j == 2:
            print(f'{j} {j}')
            flag = False
            break
        else:
            if (i-j) in sosu:
                li2.append((i-j, j))
    
    if flag:
        for k in li2:
            if k[0] > k[1]:
                if k[0]-k[1] < m:
                    m = k[0]-k[1]
                    a = k[1]
                    b = k[0]
            else:
                if k[1]-k[0] < m:
                    m = k[1]-k[0]
                    a = k[0]
                    b = k[1]
        print(f'{a} {b}')