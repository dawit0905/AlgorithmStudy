import sys
from collections import deque


def find_str(now) -> list:
    return_list = []
    for i in range(len(now)):
        num = int(now[i])
        while num > 0:
            num -= 1
            return_list.append(now[:i] + str(num) + now[i+1:])

        num = int(now[i])
        while num < 9:
            num += 1
            return_list.append(now[:i] + str(num) + now[i+1:])

    return return_list


def bfs(start, end):
    visited = [0] * 10001
    que = deque()
    que.append((start, 0))
    visited[int(start)] = 1

    while que:
        now, cnt = que.popleft()

        if now == end:
            print(cnt)
            return

        list_str = find_str(now)
        for i in list_str:
            if arr[int(i)] and not visited[int(i)] and int(i) >= 1000:
                que.append((i, cnt + 1))
                visited[int(i)] = 1

    print('impossible')
    return


arr = [True] * (10001)
for i in range(2, 10000):
    if arr[i] == True:
        for j in range(i+i, 10000, i):
            arr[j] = False

tc = int(sys.stdin.readline())
for t in range(tc):
    start, end = map(str, sys.stdin.readline().rstrip().split())
    bfs(start, end)



