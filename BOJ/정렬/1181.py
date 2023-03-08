n = int(input())
li = []
save = []

for i in range(n):
    b = input()
    li.append(b)
    save.append((i, b))

print(sorted(save))