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


n, m = map(int, sys.stdin.readline().split())
gender = ['0'] + list(map(str, sys.stdin.readline().split()))
parent = [i for i in range(n+1)]

edges = []
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((c, a, b))
edges.sort()

result, line = 0, 0
for cost, u, v in edges:
    # 같은 사이클에 속하지않고, 젠더가 달라야 된다.
    if find(u) != find(v) and gender[u] != gender[v]:
        union(u, v)
        result += cost
        line += 1

print(result if line == n-1 else -1)


