import sys


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    ap = find(a)
    bp = find(b)

    if ap < bp:
        parent[bp] = ap
    else:
        parent[ap] = bp

while True:
    m, n = map(int, sys.stdin.readline().split())
    if m == 0 and n == 0:
        exit()

    edges = []
    for i in range(n):
        x, y, z = map(int, sys.stdin.readline().split())
        edges.append((z, x, y))

    parent = [i for i in range(m+1)]
    edges.sort()

    result = 0
    for cost, a, b in edges:
        if find(a) != find(b):
            union(a, b)
        else:
            result += cost

    print(result)
