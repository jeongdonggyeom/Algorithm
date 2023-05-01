n = int(input())
direction = list(map(str, input().split()))

x = 1
y = 1

for i in direction:
	if i == 'R':
		if x + 1 > n:
			continue
		x += 1
	elif i == 'L':
		if x - 1 < 1:
			continue
		x -= 1
	elif i == 'U':
		if y - 1 < 1:
			continue
		y -= 1
	elif i == 'D':
		if y + 1 > n:
			continue
		y += 1
		
print(y, x)