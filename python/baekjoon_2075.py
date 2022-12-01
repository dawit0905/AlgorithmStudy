import sys
import heapq


n = int(sys.stdin.readline())

arr = []
for i in range(n):
    for i in list(map(int, sys.stdin.readline().split())):
        heapq.heappush(arr, i)
    while len(arr) > n:
        heapq.heappop(arr)

print(arr[0])
