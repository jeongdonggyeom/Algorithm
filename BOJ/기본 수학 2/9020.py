# 다 못품


import sys

a = int(sys.stdin.readline().rstrip())
li = []

for i in range(0, a):
    b = int(sys.stdin.readline().rstrip())
    li.append(b)

prime = [1 for i in range(max(li)+1)]

for i in range(2, max(li)+1):
    for j in range(i*2, max(li)+1, i):
        prime[j] = 0

sosu = [i for i in range(2, len(prime)) if prime[i]==1]
sosu.sort(reverse=True)

for i in li:
    li2 = [0, 0]
    for j in sosu:
        if(i/j==2):
            li2[0] = j
            li2[1] = j
            break
        elif((i-j)>=2):
            li2.append(j)
            i-=j
    print(li2)