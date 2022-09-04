import sys


x, y = map(int, sys.stdin.readline().split())

start = 0
end = 1000000000
z = (y*100) // x
answer = 0
while start <= end:
    mid = (start+end) // 2

    if z < (y + mid) * 100 // (x + mid):
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer if answer != 0 else -1)
