a, b, c = map(int, input().split())
li = [a,b,c]

ma = max(li)
mi = min(li)
li.pop(li.index(ma))
li.pop(li.index(mi))

while li[0]+mi <= ma:
    ma -= 1

print(li[0] + mi + ma)