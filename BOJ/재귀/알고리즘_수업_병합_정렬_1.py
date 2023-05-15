import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

n, k = map(int, input().split())
li = list(map(int, input().split()))
li2 = []

def merge(li, start, mid, end):
    i = start
    j = mid + 1
    tmp = []

    while i <= mid and j <= end:
        if li[i] <= li[j]:
          tmp.append(li[i])
          li2.append(li[i])
          i += 1
        else:
            tmp.append(li[j])
            li2.append(li[j])
            j += 1
    while i <= mid:
        tmp.append(li[i])
        li2.append(li[i])
        i += 1
    while j <= end:
        tmp.append(li[j])
        li2.append(li[j])
        j += 1

    i = start
    t = 0
    while i <= end:
        li[i] = tmp[t]
        i += 1
        t += 1

def sort(start, end, li):  
    if(start < end):
        mid = (start + end) // 2
        sort(start, mid, li)
        sort(mid+1, end, li)
        merge(li, start, mid, end)
    
sort(0, len(li)-1, li)

if len(li2) >= k:
    print(li2[k-1])
else:
    print(-1)