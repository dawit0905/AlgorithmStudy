import sys
import heapq

# x = int(sys.stdin.readline())
# answer = bin(x)
# print(str(answer)[2:].count('1'))


x = int(sys.stdin.readline())
que = []

heapq.heappush(que, 64)
_sum = 64

while _sum > x:
    half = que[0] // 2
    heapq.heappop(que)

    heapq.heappush(que, half)
    heapq.heappush(que, half)

    if _sum - half >= x:
        temp = que[0]
        _sum -= temp
        heapq.heappop(que)


print(len(que))
