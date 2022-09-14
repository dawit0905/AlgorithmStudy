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


n = int(sys.stdin.readline())
parent = [i for i in range(n+1)]

temp = []
for i in range(n):
    x, y, z = map(int, sys.stdin.readline().split())
    temp.append([x, y, z, i])

edges = []
for i in range(3):
    temp.sort(key=lambda x: x[i])
    for j in range(1, n):
        edges.append((abs(temp[j-1][i]-temp[j][i]), temp[j-1][3], temp[j][3]))
# 전체 노드를 담게 되면 메모리/시간 초과가 난다.
# for i in range(n-1):
#     for j in range(i+1, n):
#         cost = min(abs(temp[i][0]-temp[j][0]), abs(temp[i][1]-temp[j][1]), abs(temp[i][2]-temp[j][2]))
#         edges.append((cost, i, j))

edges.sort()
result = 0
for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        result += cost

print(result)
