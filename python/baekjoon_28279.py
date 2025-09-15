import sys
from collections import deque


n = int(sys.stdin.readline())
que = deque([])

for i in range(n):
    arr = list(map(int, sys.stdin.readline().split()))

    if len(arr) == 1:
        N = arr[0]
    else:
        N, x = arr[0], arr[1]

    if N == 1:
        que.appendleft(x)
    if N == 2:
        que.append(x)
    if N == 3:
        if que:
            print(que.popleft())
        else:
            print(-1)
    if N == 4:
        if que:
            print(que.pop())
        else:
            print(-1)
    if N == 5:
        print(len(que))
    if N == 6:
        if que:
            print(0)
        else:
            print(1)
    if N == 7:
        if que:
            print(que[0])
        else:
            print(-1)
    if N == 8:
        if que:
            print(que[-1])
        else:
            print(-1)



