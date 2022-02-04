import heapq
import sys

n = int(sys.stdin.readline())
max_heap = []
for i in range(n):
    input_num = int(sys.stdin.readline())
    if input_num == 0:
        if max_heap:
            print(-heapq.heappop(max_heap))
        else:
            print(0)
    else:
        heapq.heappush(max_heap, -input_num)

