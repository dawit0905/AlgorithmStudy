import sys


def find(parent, x) -> int:
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b) -> None:
    pa = find(parent, a)
    pb = find(parent, b)

    if arr[pa] <= arr[pb]:
        parent[pb] = pa
    else:
        parent[pa] = pb


n, m, k = map(int, sys.stdin.readline().split())
arr = [0] + list(map(int, sys.stdin.readline().split()))
parent = [i for i in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    union(parent, a, b)

friends = set()
cost = 0
for i in range(1, n+1):
    if find(parent, i) not in friends:
        cost += arr[parent[i]]
        friends.add(parent[i])

if cost <= k:
    print(cost)
else:
    print('Oh no')
