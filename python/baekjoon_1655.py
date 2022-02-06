import heapq
import sys

left, right = [],[]
n = int(sys.stdin.readline())

for _ in range(n):
    num = int(sys.stdin.readline())
    if len(left) == len(right):
        heapq.heappush(left,(-num,num))
    else:
        heapq.heappush(right, (num,num))

    if right and left[0][1] > right[0][1]:
        var_left = heapq.heappop(left)[1]
        var_right = heapq.heappop(right)[1]
        heapq.heappush(right, (var_left, var_left))
        heapq.heappush(left, (-var_right, var_right))

    print(left[0][1])