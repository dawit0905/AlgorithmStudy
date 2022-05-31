import sys
from collections import deque

n, w, l = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

que = deque([0]*w)

index = 0
cnt = 0
while que:
    a = que.popleft()
    cnt += 1
    if index < n:
        if sum(que)+arr[index]<=l:
            que.append(arr[index])
            index += 1
        else:
            que.append(0)

print(cnt)
