import heapq
import sys

n = int(sys.stdin.readline())
q = []
for i in range(n):
    input_num = int(sys.stdin.readline())

    if input_num == 0:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q)[1])
    else:
        heapq.heappush(q, (abs(input_num), input_num))
