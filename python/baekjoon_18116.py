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
        size[ap] += size[bp]
        size[bp] = 0
    elif bp < ap:
        parent[ap] = bp
        size[bp] += size[ap]
        size[ap] = 0


n = int(sys.stdin.readline())
parent = [i for i in range(int(10**6)+1)]
size = [1 for i in range(int(10**6)+1)]
for _ in range(n):
    arr = sys.stdin.readline().strip().split()

    if arr[0] == 'I':
        a, b = int(arr[1]), int(arr[2])
        union(parent, a, b)
    else:
        x = int(arr[1])
        pc = find(parent, x)
        print(size[pc])