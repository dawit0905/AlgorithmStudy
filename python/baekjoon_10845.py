import sys
from collections import deque

n = int(sys.stdin.readline())
que = deque()

for i in range(n):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'push':
        num = int(cmd[1])
        que.append(num)
    elif cmd[0] == 'pop':
        if que:
            num = que.popleft()
            print(num)
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(que))
    elif cmd[0] == 'empty':
        if que:
            print(0)
        else :
            print(1)
    elif cmd[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)