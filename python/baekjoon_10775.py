import sys


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


g = int(sys.stdin.readline())
p = int(sys.stdin.readline())
edges = []
result = 0
parent = [i for i in range(g+1)]
for i in range(p):
    edges.append(int(sys.stdin.readline()))

for i in edges:
    x = find(parent, i)
    if x == 0:
        break
    union(parent,x,x-1)
    result += 1
print(result)
