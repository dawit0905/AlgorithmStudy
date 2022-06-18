import sys


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    ap = find(parent, a)
    bp = find(parent, b)

    if ap != bp:
        parent[bp] = ap
        size[ap] += size[bp]
        size[bp] = 0


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    name_to_number = {}
    cnt = 1
    parent = [i for i in range(n*2+1)]
    size = [1 for i in range(n*2+1)]
    for _ in range(n):
        f1, f2 = list(map(str, sys.stdin.readline().rstrip().split()))
        if f1 not in name_to_number:
            name_to_number[f1] = cnt
            cnt += 1

        if f2 not in name_to_number:
            name_to_number[f2] = cnt
            cnt += 1

        ap = find(parent, name_to_number[f1])
        bp = find(parent, name_to_number[f2])

        if ap == bp:
            print(max(size[ap], size[bp]))
        else:
            union(parent, ap, bp)
            print(max(size[ap], size[bp]))
