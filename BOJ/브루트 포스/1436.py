import sys

n = int(sys.stdin.readline())

end = 665
cnt = 0

while True:
    end += 1
    number = str(end)

    for i in range(len(number)-2):
        if number[i] == '6' and number[i+1] == '6' and number[i+2] == '6':
            cnt += 1
            break

    if cnt == n:
        print(end)
        break
