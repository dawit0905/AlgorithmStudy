import sys


def parent_find(parent, x):
    if parent[x] != x:
        parent[x] = parent_find(parent, parent[x])
    return parent[x]


def parent_union(parent, a, b):
    a = parent_find(parent, a)
    b = parent_find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


sys.setrecursionlimit(1000000)
n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n+1)]

for i in range(m):
    cmd, a, b = map(int, sys.stdin.readline().split())

    if cmd == 0:
        parent_union(parent, a, b)
    else:
        if parent_find(parent, a) == parent_find(parent, b):
            print('YES')
        else:
            print('NO')

