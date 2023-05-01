li = list(map(int, input().split()))
w = []
h = []

for i in range(0, len(li), 2):
	if li[i] < li[i+1]:
		w.append(li[i+1])
		h.append(li[i])
	else:
		w.append(li[i])
		h.append(li[i+1])
	
print(max(w)*max(h))