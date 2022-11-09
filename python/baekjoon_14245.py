import sys


def init(arr, tree, node, start, end) -> None:
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start+end) // 2
        init(arr, tree, node*2, start, mid)
        init(arr, tree, node*2+1, mid+1, end)
        tree[node] = tree[node*2] ^ tree[node*2+1]


def query(tree, lazy, node, start, end, left, right) -> int:
    update_lazy(tree, lazy, node, start, end)

    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]


    mid = (start+end)//2
    lsum = query(tree, lazy, node*2, start, mid, left, right)
    rsum = query(tree, lazy, node*2+1, mid+1, end, left, right)
    return lsum ^ rsum


def update_range(tree, lazy, node, start, end, left, right, diff) -> None:
    update_lazy(tree, lazy, node, start, end)

    if left > end or right < start:
        return

    if left <= start and end <= right:
        tree[node] ^= diff

        if start != end:
            lazy[node*2] ^= diff
            lazy[node*2+1] ^= diff

        return

    mid = (start+end)//2
    update_range(tree, lazy, node*2, start, mid, left, right, diff)
    update_range(tree, lazy, node*2+1, mid+1, end, left, right, diff)
    tree[node] = tree[node*2] ^ tree[node*2+1]


def update_lazy(tree, lazy, node, start, end) -> None:
    if lazy[node] != 0:
        tree[node] ^= lazy[node]

        if start != end:
            lazy[node*2] ^= lazy[node]
            lazy[node*2+1] ^= lazy[node]
        lazy[node] = 0


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
tree_size = n * 4
tree = [0] * tree_size
lazy = [0] * tree_size
init(arr, tree, 1, 0, n-1)

m = int(sys.stdin.readline())
for i in range(m):
    flag, *q = map(int, sys.stdin.readline().split())

    if flag == 1:
        left, right, diff = q
        update_range(tree, lazy, 1, 0, n-1, left, right, diff)
    else:
        x = q[0]
        print(query(tree, lazy, 1, 0, n-1, x, x))
