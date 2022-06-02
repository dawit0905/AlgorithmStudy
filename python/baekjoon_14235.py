import sys
import heapq

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    if a[0]==0:
        if len(arr) == 0:
            print(-1)
        else:
            print(-heapq.heappop(arr))
    else:
        for i in range(a[0]):
            heapq.heappush(arr, -a[i+1])