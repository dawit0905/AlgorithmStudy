import sys


def init(arr, tree, node, start, end):
    if start == end:
        if arr[start]%2 == 0:
            tree[node][0] = 1
        else:
            tree[node][1] = 1
        return
    init(arr, tree, node*2, start, (start+end)//2)
    init(arr, tree, node*2+1, (start+end)//2+1, end)
    tree[node] = [tree[node * 2][0] + tree[node * 2 + 1][0], tree[node * 2][1] + tree[node * 2 + 1][1]]


def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return [0, 0]

    if left <= start and right >= end:
        return tree[node]

    lnode = query(tree, node*2, start, (start+end)//2, left, right)
    rnode = query(tree, node*2+1, (start+end)//2+1, end, left, right)
    return [lnode[0] + rnode[0], lnode[1] + rnode[1]]


def update(arr, tree, node, start, end, index, val):
    if start > index or end < index:
        return

    if start == end:
        arr[index] = val
        if val%2 == 0:
            tree[node] = [1, 0]
        else:
            tree[node] = [0, 1]

        return

    update(arr, tree, node*2, start, (start+end)//2, index, val)
    update(arr, tree, node*2+1, (start+end)//2+1, end, index, val)
    tree[node] = [tree[node*2][0] + tree[node*2+1][0], tree[node*2][1] + tree[node*2+1][1]]


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
tree = [[0, 0] for _ in range(n*4)]

init(arr, tree, 1, 0, n-1)
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())

    if a == 1:
        update(arr, tree, 1, 0, n-1, b-1, c)
    elif a == 2:
        print(query(tree, 1, 0, n-1, b-1, c-1)[0])
    else:
        print(query(tree, 1, 0, n-1, b-1, c-1)[1])
