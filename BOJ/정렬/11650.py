n = int(input())
li = []
for _ in range(n):
    x, y = map(int, input().split())
    li.append((x, y))

for i in sorted(li):
    print(f'{i[0]} {i[1]}')