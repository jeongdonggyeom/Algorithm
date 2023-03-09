n = int(input())
li = []

for i in range(n):
    a, b = map(str, input().split())
    li.append((int(a),i,b))

for i in sorted(li):
    print(f'{i[0]} {i[2]}')