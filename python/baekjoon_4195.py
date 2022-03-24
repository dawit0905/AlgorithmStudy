import sys


def parent_find(parent, x):
    if parent[x] == x:
        return x
    else:
        root_x = parent_find(parent, parent[x])
        parent[x] = root_x
        return parent[x]


def parent_union(parent, a, b):
    root_a = parent_find(parent, a)
    root_b = parent_find(parent, b)

    if root_a != root_b:
        parent[root_b] = root_a
        number[root_a] += number[root_b]


T = int(sys.stdin.readline())

for _ in range(T):
    F = int(sys.stdin.readline())
    parent = {}
    number = {}
    for _ in range(F):
        a, b = map(str, sys.stdin.readline().split())

        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1

        parent_union(parent, a, b)

        print(number[parent_find(parent, a)])
