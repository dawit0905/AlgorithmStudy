import sys
import heapq


n = int(sys.stdin.readline())
arr = []
now = 0
for i in range(n):
    num = int(sys.stdin.readline())
    if i == 0:
        now = num
        continue
    heapq.heappush(arr, (-num, i))


if n == 1:
    print(0)
    exit(0)

cnt = 0
while True:
    num, index = heapq.heappop(arr)
    num = abs(num)
    if now == num:
        cnt += 1
        print(cnt)
        break
    elif now > num:
        print(cnt)
        break
    elif now < num:
        now += 1
        num -= 1
        cnt += 1

        heapq.heappush(arr, (-num, index))

