import sys


def recur(arr, depth):
    mid = len(arr) // 2
    tree[depth].append(arr[mid])
    if len(arr) == 1:
        return

    recur(arr[:mid], depth + 1)
    recur(arr[mid + 1:], depth + 1)


k = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

tree = [[] for _ in range(k)]

recur(arr, 0)

for i in tree:
    print(*i)
