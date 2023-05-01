pan = [[0 for _ in range(8)] for _ in range(8)]
direction = [(-2, -1), (2, 1), (-2, 1), (2, -1), (-1, -2), (1, 2), (-1, 2), (1, -2)]

a = input()

x = ord(a[0])-96
y = int(a[1])
cnt = 0

for i in direction:
	cx = x+i[0]
	cy = y+i[1]
	
	if cx < 1 or cx > 8 or cy < 1 or cy > 8:
		continue
	
	cnt += 1
	
print(cnt)