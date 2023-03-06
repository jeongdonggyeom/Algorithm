a = int(input())

li = ["" for _ in range(a)]

for i in range(a):
    li[i] = input()

for i in range(a):
    print(f'{li[i][0]}{li[i][-1]}')