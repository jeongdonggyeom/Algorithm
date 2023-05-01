b, y = map(int, input().split())
li = []
m, f, s = 100000000, 0, 0

if y == 1:
    print(3, 3)

else:
    for i in range(1, y+1):
        if y % i == 0:
            li.append(i)

    for i in range(len(li)//2):
        if m > li[-i] - li[i]:
            f, s = li[i], li[-(i+1)]

    print(s+2, f+2)