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
        force[ap] += force[bp]
    else:
        parent[ap] = bp
        force[bp] += force[ap]


def fight(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if force[a] > force[b]:
        force[a] -= force[b]
        parent[b] = a
    elif force[a] < force[b]:
        force[b] -= force[a]
        parent[a] = b
    else:  # 두 나라의 병력이 같은 경우
        parent[a] = 0
        parent[b] = 0
        

sys.setrecursionlimit(10**6)
n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n+1)]
force = [0] * (n+1)
for i in range(1, n+1):
    num = int(sys.stdin.readline())
    force[i] = num

for i in range(m):
    o, p, q = map(int, sys.stdin.readline().split())

    if o == 1:
        union(parent, p, q)
    else:
        fight(parent, p, q)


s = set()
for i in range(1, n+1):
    num = find(parent, i)
    if num != 0:
        s.add(num)

answer = []
for i in s:
    answer.append(force[i])
answer.sort()
print(len(answer))
print(*answer)

