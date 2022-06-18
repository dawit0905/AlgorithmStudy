import sys


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    ap = find(parent, a)
    bp = find(parent, b)

    if (ap < bp):
        parent[bp] = ap
    else:
        parent[ap] = bp


n, m = map(int, sys.stdin.readline().split())
answer = 0
parent = [i for i in range(n)]
for idx in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
    else:
        answer = idx + 1
        break

print(answer)
