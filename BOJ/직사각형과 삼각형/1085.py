x,y,w,h = map(int, input().split())
li = []

li.append(x)
li.append(y)
li.append(h-y)
li.append(w-x)

print(min(li))