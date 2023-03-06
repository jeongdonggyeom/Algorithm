while True:
    n = int(input())
    if n == -1:
        break

    li = []
    for i in range(1, n):
        if n%i == 0:
            li.append(i)
    if n == sum(li):
        print(f'{n} = {li[0]}', end="")
        for i in range(1, len(li)):
            print(f' + {li[i]}', end="")
        print()
    else:
        print(f'{n} is NOT perfect.')