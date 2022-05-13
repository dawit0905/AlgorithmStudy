import sys
from collections import deque

n = int(sys.stdin.readline())

apple = []
k = int(sys.stdin.readline())
for i in range(k):
    a, b = map(int, sys.stdin.readline().split())
    apple.append([a, b])

direction = {}
L = int(sys.stdin.readline())
for i in range(L):
    a, b = sys.stdin.readline().rstrip().split()
    direction[int(a)] = b

body = deque()
body.append([1, 1])
now_body = [0,1]
head = [1,1]
left = [[1,0],[0,1],[-1,0],[0,-1]]
right = [[1,0],[0,-1],[-1,0],[0,1]]
time = 0
while True:

    if time in direction:
        if direction[time] == 'L':
            idx = left.index(now_body)
            if len(left) == idx+1:
                now_body = left[0]
            else:
                now_body = left[idx+1]
        else:
            idx = right.index(now_body)
            if len(right) == idx+1:
                now_body = right[0]
            else:
                now_body = right[idx+1]
    head = [head[0] + now_body[0], head[1] + now_body[1]]
    time += 1
    if head in apple:
        body.appendleft(head)
        idx = apple.index(head)
        apple = apple[:idx] + apple[idx+1:]
    else:
        if head[0] < 1 or head[0] > n or head[1] < 1 or head[1] > n or (head in body):
            print(time)
            break

        body.appendleft(head)
        body.pop()


