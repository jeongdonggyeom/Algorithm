li = [list(map(int, input().split())) for _ in range(9)]

maximum = 0
for i in li:
    maxi = max(i)
    if maximum < maxi:
        maximum = maxi
    
idx = [[i+1, j+1] for i in range(9) for j in range(9) if li[i][j] == maximum]

print(maximum)
print(f'{idx[0][0]} {idx[0][1]}')