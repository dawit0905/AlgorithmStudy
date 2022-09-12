import sys
import math


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    ap = find(parent, a)
    bp = find(parent, b)

    if ap < bp:
        parent[bp] = ap
    else:
        parent[ap] = bp


n = int(sys.stdin.readline())
temp = []
parent = [i for i in range(n+1)]
for i in range(n):
    x, y = map(float, sys.stdin.readline().split())
    temp.append((x, y))

edges = []
for i in range(n-1):
    for j in range(i+1, n):
        a, b = temp[i][0], temp[i][1]
        c, d = temp[j][0], temp[j][1]
        cost = ((c-a)**2+(d-b)**2)**0.5
        edges.append((cost, i, j))

edges.sort()
result = 0
for cost, a, b in edges:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

print(round(result, 2))
