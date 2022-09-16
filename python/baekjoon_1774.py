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
temp = [0] # parent에서 node 시작을 1로 하기위해서?
parent = [i for i in range(n+1)]
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    temp.append((a, b))

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    union(a, b)

edges = []
for i in range(1, n):
    for j in range(i+1, n+1):
        cost = (abs(temp[i][0]-temp[j][0]) ** 2 + abs(temp[i][1] - temp[j][1])** 2) ** 0.5
        edges.append((cost, i, j))

edges.sort()
result = 0
for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        result += cost

print("{:.2f}".format(result))