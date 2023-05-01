n = int(input())
li = list(map(int, input().split()))
c = int(input())
cnt = 0

def aspoasp(sum, depth):
    global cnt
    if depth == n:
        if sum == c:
            cnt += 1
        return
    else:
        aspoasp(sum + li[depth], depth+1)
        aspoasp(sum - li[depth], depth+1)

aspoasp(0, 0)
print(cnt)