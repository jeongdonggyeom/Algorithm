n = int(input())
li = []
for _ in range(n):
    x, y = map(int, input().split())
    li.append((y, x))

for i in sorted(li):
    print(f'{i[1]} {i[0]}')