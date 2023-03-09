n = int(input())
li = []

for _ in range(n):
    li.append(input())

li = sorted(list(set(li)))
li.sort(key=len)

for i in li:
    print(i)