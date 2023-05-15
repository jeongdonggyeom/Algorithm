n = int(input())
li = []

def hanoi(n, f, t, a):
    if n == 1:
        li.append((f, t))
        return
    hanoi(n-1, f, a, t)
    li.append((f, t))
    hanoi(n-1, a, t, f)

hanoi(n, 1, 3, 2)
print(len(li))
for i in li:
    print(f'{i[0]} {i[1]}')