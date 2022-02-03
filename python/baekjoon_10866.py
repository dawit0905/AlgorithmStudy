import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque()
for i in range(n):
    cmd_list = sys.stdin.readline().split()

    if cmd_list[0] == 'push_front':
        q.appendleft(int(cmd_list[1]))
    elif cmd_list[0] == 'push_back':
        q.append(int(cmd_list[1]))
    elif cmd_list[0] == 'pop_front':
        if len(q) > 0:
            print(q.popleft())
        else :
            print(-1)
    elif cmd_list[0] == 'pop_back':
        if len(q) > 0:
            print(q.pop())
        else:
            print(-1)
    elif cmd_list[0] == 'size':
        print(len(q))
    elif cmd_list[0] == 'empty':
        if len(q) > 0:
            print(0)
        else :
            print(1)
    elif cmd_list[0] == 'front':
        if len(q) > 0:
            print(q[0])
        else :
            print(-1)
    elif cmd_list[0] == 'back':
        if len(q) > 0:
            print(q[-1])
        else :
            print(-1)