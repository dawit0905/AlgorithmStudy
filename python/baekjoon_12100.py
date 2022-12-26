import sys
import copy
from collections import deque


def get(i, j):
    if arr[i][j]:
        que.append(arr[i][j])
        arr[i][j] = 0


def merge(i, j, di, dj):
    while que:
        x = que.popleft()
        if not arr[i][j]:
            arr[i][j] = x
        elif arr[i][j] == x:
            arr[i][j] = x * 2
            i, j = i + di, j + dj
        else:
            i, j = i + di, j + dj
            arr[i][j] = x


def move(k):
    if k == 0:
        for j in range(n):
            for i in range(n):
                get(i, j)
            merge(0, j, 1, 0)
    elif k == 1:
        for j in range(n):
            for i in range(n - 1, -1, -1):
                get(i, j)
            merge(n - 1, j, -1, 0)
    elif k == 2:
        for i in range(n):
            for j in range(n):
                get(i, j)
            merge(i, 0, 0, 1)
    else:
        for i in range(n):
            for j in range(n - 1, -1, -1):
                get(i, j)
            merge(i, n - 1, 0, -1)

def dfs(depth):
    global answer, arr
    if depth == 5:
        for i in range(n):
            answer = max(answer, max(arr[i]))
        return

    board = copy.deepcopy(arr)

    for i in range(4):
        move(i)
        dfs(depth+1)
        arr = copy.deepcopy(board)


n = int(sys.stdin.readline())
answer = 0
que = deque()
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dfs(0)
print(answer)
