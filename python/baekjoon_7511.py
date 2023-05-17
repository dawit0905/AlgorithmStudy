import sys


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    ap = find(parent, a)
    bp = find(parent, b)

    if ap > bp:
        parent[ap] = bp
    else:
        parent[bp] = ap



t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    k = int(sys.stdin.readline())
    parent = [j for j in range(n)]
    for j in range(k):
        a, b = map(int, sys.stdin.readline().split())
        union(parent, a, b)

    print(f'Scenario {i+1}:')
    m = int(sys.stdin.readline())
    for j in range(m):
        a, b = map(int, sys.stdin.readline().split())

        if find(parent, a) == find(parent, b):
            print(1)
        else:
            print(0)

    print()
