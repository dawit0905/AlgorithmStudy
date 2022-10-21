import sys


def update(tree, node, target, diff, start, end):

    if target < start or target > end:
        return

    tree[node] += diff
    if start == end:
        return

    mid = (start + end) // 2
    update(tree, node * 2, target, diff, start, mid)
    update(tree, node * 2 + 1, target, diff,  mid+1, end)


def query(tree, node, target, start, end):
    if start == end:
        return start

    mid = (start+end) // 2
    if target <= tree[node * 2]:
        return query(tree, node * 2, target, start, mid)
    else:
        return query(tree, node * 2+1, target - tree[node*2], mid+1, end)


MAX_SIZE = 1000001
h = MAX_SIZE * 4
tree = [0] * h
t = int(sys.stdin.readline())
for i in range(t):
    arr = list(map(int, sys.stdin.readline().split()))

    if arr[0] == 1:
        a, b = arr[0], arr[1]
        favor = query(tree, 1, b, 1, MAX_SIZE)
        print(favor)
        update(tree, 1, favor, -1, 1, MAX_SIZE)

    if arr[0] == 2:
        a, b, c = arr[0], arr[1], arr[2]
        update(tree, 1, b, c, 1, MAX_SIZE)

# 참고한 블로그
# https://ghdic.github.io/ps/boj-2243/