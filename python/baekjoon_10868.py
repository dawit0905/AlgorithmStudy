import sys
import math


def init(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        init(arr, tree, node*2, start, (start+end)//2)
        init(arr, tree, node*2+1, (start+end)//2+1, end)
        tree[node] = min(tree[node*2], tree[node*2+1])


def query(arr, tree, node, start, end, left, right):
    if left > end or right < start:
        return -1
    if left <= start and end <= right:
        return tree[node]
    lsum = query(arr, tree, node*2, start, (start+end)//2, left, right)
    rsum = query(arr, tree, node*2+1, (start+end)//2+1, end, left, right)

    if lsum == -1:
        return rsum
    elif rsum == -1:
        return lsum
    else:
        return min(lsum, rsum)


def update(arr, tree, node, start, end, index, val):
    pass


n, m = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]
h = math.ceil(math.log2(n))
tree_size = 1 << (h+1)
tree = [0] * tree_size
init(arr, tree, 1, 0, n-1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(query(arr, tree, 1, 0, n-1, a-1, b-1))