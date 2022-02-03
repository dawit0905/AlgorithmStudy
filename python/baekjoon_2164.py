from collections import deque

n = int(input())

q = deque([i for i in range(1,n+1)])

while 1:
    if len(q) == 1:
        print(q[0])
        break

    q.popleft()
    q.append(q.popleft())