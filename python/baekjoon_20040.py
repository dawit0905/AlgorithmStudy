import sys


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    global answer, idx
    ap = find(parent, a)
    bp = find(parent, b)

    if ap == bp:
        answer = idx + 1
    if (ap < bp):
        parent[bp] = ap
    else:
        parent[ap] = bp


n, m = map(int, sys.stdin.readline().split())
edges = []
answer = 0
parent = [i for i in range(n)]
for idx in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if not answer:
        union(parent, a, b)

print(answer)
