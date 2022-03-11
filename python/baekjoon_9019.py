import sys
from collections import deque


def bfs(a, b):
    que = deque()
    que.append((a, ''))

    while que:
        num, string = que.popleft()
        if int(num) == int(b):
            return string

            # D
        temp_num = (num * 2) % 10000
        if arr[int(temp_num)] == 0:
            arr[int(temp_num)] = 1
            que.append((temp_num, string+'D'))
        # S
        if num == 0:
            temp_num = 9999
        else:
            temp_num = num - 1
        if arr[temp_num] == 0:
            arr[temp_num] = 1
            que.append((temp_num, string+'S'))
        # L
        temp_num = int(num % 1000 * 10 + num / 1000)
        if arr[temp_num] == 0:
            arr[temp_num] = 1
            que.append((temp_num, string+'L'))
        # R
        temp_num = int(num % 10 * 1000 + num // 10)
        if arr[temp_num] == 0:
            arr[temp_num] = 1
            que.append((temp_num, string+'R'))


T = int(sys.stdin.readline())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    arr = [0 for i in range(10000)]
    answer = bfs(a, b)
    print(answer)