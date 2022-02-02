from collections import deque
import sys
q = deque()

n = int(sys.stdin.readline())
for _ in range(n):
    array = sys.stdin.readline().rstrip().split()

    if array[0] == 'push':
        q.append(int(array[1]))
    elif array[0] == 'front':
        if len(q) > 0:
            print(q[0])
        else :
            print(-1)
    elif array[0] == 'back':
        if len(q) > 0:
            print(q[-1])
        else:
            print(-1)
    elif array[0] == 'size':
        print(len(q))
    elif array[0] == 'empty':
        if len(q) > 0:
            print(0)
        else :
            print(1)
    elif array[0] == 'pop':
        if len(q) > 0:
            print(q.popleft())
        else :
            print(-1)