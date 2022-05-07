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

n, m = map(int, sys.stdin.readline().split())
result = 0

knower = list(map(int, sys.stdin.readline().split()))[1:]
parent = [j for j in range(n+1)]
stranger = []
for i in range(m):
    temp = list(map(int, sys.stdin.readline().split()))
    stranger.append(temp[1:])

    if temp[0] >= 2:
        for j in range(2, len(temp)):
            if find(parent, temp[j - 1] != find(parent, temp[j])):
                union(parent, temp[j - 1], temp[j])

for j in stranger:
    flag = 1
    for t in knower:
        if find(parent, j[0]) == find(parent, t):
            flag = 0
    if flag:
        result += 1

print(result)
