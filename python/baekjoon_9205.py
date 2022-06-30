import sys
from collections import deque


def bfs(home, store, festival) -> bool:
    x, y = home[0], home[1]
    que = deque()
    que.append((x, y))

    while que:
        x, y = que.popleft()

        if abs(x - festival[0]) + abs(y - festival[1]) <= 1000:
            print('happy')
            return

        remove_list = []
        for i in store:
            nx = abs(x-i[0])
            ny = abs(y-i[1])
            if (nx+ny) <= 1000:
                que.append([i[0], i[1]])
                remove_list.append(i)
        for i in remove_list:
            store.remove(i)
            
    print('sad')


t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    home = list(map(int, sys.stdin.readline().split()))
    store = []
    for j in range(n):
        store.append(list(map(int, sys.stdin.readline().split())))
    festival = list(map(int, sys.stdin.readline().split()))

    bfs(home, store, festival)
