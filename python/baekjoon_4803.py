import sys


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


idx = 0
while True:
    idx += 1
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        exit(0)

    parent = [i for i in range(n+1)]
    cycle = set()
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        if find(parent, a) == find(parent, b):
            cycle.add(parent[a])
            cycle.add(parent[b])
        if parent[a] in cycle or parent[b] in cycle:
            cycle.add(parent[a])
            cycle.add(parent[b])
        union(parent, a, b)

    for i in range(n+1):
        find(parent, i)

    parent = set(parent)
    ans = sum([1 if i not in cycle else 0 for i in parent]) - 1
    if ans == 0:
        print('Case %d: No trees.' % idx)
    elif ans == 1:
        print('Case %d: There is one tree.' % idx)
    else:
        print('Case %d: A forest of %d trees.' % (idx, ans))
