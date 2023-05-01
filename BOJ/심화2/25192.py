n = int(input())

cnt = 0
s = set()

for i in range(n):
    a = input()
    if a == "ENTER":
        cnt += len(s)
        s.clear()
    else:
        s.add(a)

cnt += len(s)

print(cnt)