t = int(input())

m = [0] * 101

for i in range(t):
    n = int(input())
    m[0] = m[1] = m[2] = 1
    for i in range(3, n):
        m[i] = m[i-2] + m[i-3]
    print(m[n-1])