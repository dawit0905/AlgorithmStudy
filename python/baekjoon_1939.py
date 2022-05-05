import sys


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    ap = find(parent, a)
    bp = find(parent, b)

    if ap < bp:
        parent[ap] = bp
    else:
        parent[bp] = ap


n, m = map(int, sys.stdin.readline().split())
parent = [0] * (n+1)
edges = []
for i in range(n+1):
    parent[i] = i

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((c, a, b))

ta, tb = map(int, sys.stdin.readline().split())

edges.sort(reverse=True)
for cost, a, b in edges:

    union(parent, a, b)
    if find(parent, ta) == find(parent, tb):
        print(cost)
        break