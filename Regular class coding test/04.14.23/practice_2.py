array = list(map(int, input().split()))
commands = list(map(int, input().split()))
sort_array = []


def ssss(li):
	for i in range(1, len(li)):
		for j in range(i, 0, -1):
			if li[j] < li[j-1]:
				li[j], li[j-1] = li[j-1], li[j]
			else:
				break


def hhhh(start, end, target, li):
	newLi = li[start:end]
	ssss(newLi)
	return newLi[target]


for i in range(0, len(commands), 3):
    sort_array.append(
    	hhhh(commands[i]-1, commands[i+1], commands[i+2]-1, array))

for i in sort_array:
	print(i, end=" ")
