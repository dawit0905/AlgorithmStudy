import sys


def find(x, parent):
    if parent[x] == -1:
        return 1
    elif parent[x] == -2:
        return -2
    else:
        return find(parent[x], parent)


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
remove_node = int(sys.stdin.readline())
arr[remove_node] = -2

cnt = 0
for i in range(n):
    if find(i, arr) == 1 and i not in arr:
        cnt += 1

print(cnt)

