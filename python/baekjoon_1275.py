import sys
import math


def init(arr, segtree, node, start, end):
    if start == end:
        segtree[node] = arr[start]
    else:
        init(arr, segtree, node*2, start, (start+end)//2)
        init(arr, segtree, node*2+1, (start+end)//2+1, end)
        segtree[node] = segtree[node*2] + segtree[node*2+1]


def query(segtree, node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return segtree[node]
    lsum = query(segtree, node*2, start, (start+end)//2, left, right)
    rsum = query(segtree, node*2+1, (start+end)//2+1, end, left, right)
    return lsum + rsum


def update(arr, segtree, node, start, end, index, val):
    if index < start or index > end:
        return
    if start == end:
        arr[index] = val
        segtree[node] = val
        return
    update(arr, segtree, node*2, start, (start+end)//2, index, val)
    update(arr, segtree, node*2+1, (start+end)//2+1, end, index, val)
    segtree[node] = segtree[node*2] + segtree[node*2+1]


n, q = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

h = math.ceil(math.log2(n))
tree_size = 1 << (h+1)
segtree = [0] * tree_size
init(arr, segtree, 1, 0, n-1)

for i in range(q):
    x, y, a, b = map(int, sys.stdin.readline().split())
    if x <= y:
        print(query(segtree, 1, 0, n - 1, x - 1, y - 1))
    else:
        print(query(segtree, 1, 0, n - 1, y - 1, x - 1))

    update(arr, segtree, 1, 0, n-1, a-1, b)
