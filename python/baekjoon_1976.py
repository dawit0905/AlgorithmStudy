import sys


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
parent = [i for i in range(n+1)]

for i in range(1, n+1):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(1, len(temp)+1):
        if temp[j-1] == 1:
            union_parent(parent, i, j)

plan = list(map(int, sys.stdin.readline().split()))
result = []
for i in plan:
    result.append(find_parent(parent, i))

if len(set(result)) == 1:
    print("YES")
else:
    print("NO")

