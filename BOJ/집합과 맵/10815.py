import sys
input = sys.stdin.readline

n = int(input())
li = sorted(list(map(int, input().split())))

m = int(input())
card = list(map(int, input().split()))

def binary_search(target):
    start = 0
    end = n-1

    while start <= end:
        mid = (start+end) // 2

        if li[mid] == target:
            return True
        elif li[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False

for i in card:
    if binary_search(i):
        print(1, end=" ")
    else:
        print(0, end=" ")
