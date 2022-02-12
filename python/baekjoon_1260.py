import sys
from collections import deque

'''
4 5 1
1 2
1 3
1 4
2 4
3 4
'''


def dfs(start):
    # 이미 방문했으면
    if dfs_visited[start]:
        return
    print(start, end=" ")
    dfs_visited[start] = 1

    for i in range(len(dfs_data[start])):
        dfs(min(dfs_data[start]))
        dfs_data[start].remove(min(dfs_data[start]))


def bfs(start):
    que.append(start)
    while que:
        temp = que.popleft()
        if bfs_visited[temp] == 1:
            continue
        bfs_visited[temp] = 1

        print(temp, end=" ")

        for i in range(len(bfs_data[temp])):
            que.append(min(bfs_data[temp]))
            bfs_data[temp].remove(min(bfs_data[temp]))


n, m, v = map(int, sys.stdin.readline().split())
dfs_data = [[] for i in range(n + 1)]
dfs_visited = [0 for i in range(n + 1)]
bfs_data = [[] for i in range(n + 1)]
bfs_visited = [0 for i in range(n + 1)]
que = deque()

for i in range(m):
    start, end = map(int, sys.stdin.readline().split())
    # 양방향이니까 둘다 넣어줘야됨.
    dfs_data[start].append(end)
    dfs_data[end].append(start)
    bfs_data[start].append(end)
    bfs_data[end].append(start)

dfs(v)
print()
bfs(v)
# print(dfs_data) [[], [2, 3, 4], [4], [4], []]

