import sys
import heapq

n = int(sys.stdin.readline())
que = []

for i in range(n):
    heapq.heappush(que, int(sys.stdin.readline()))

if len(que) == 1:
    print(0)
else:
    answer = 0
    while len(que) > 1:
        a = heapq.heappop(que)
        b = heapq.heappop(que)
        answer += a + b
        heapq.heappush(que, a+b)

    print(answer)