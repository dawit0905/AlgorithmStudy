import sys
import math
DIV = 1000000007

def init(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        init(arr, tree, node*2, start, (start+end)//2)
        init(arr, tree, node*2+1, (start+end)//2+1, end)
        tree[node] = (tree[node*2] * tree[node*2+1]) % DIV


def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[node]
    lsum = query(tree, node * 2, start, (start + end) // 2, left, right)
    rsum = query(tree, node * 2 + 1, (start + end) // 2 + 1, end, left, right)
    return (lsum * rsum) % DIV

def update(arr, tree, node, start, end, index, val):
    if index < start or index > end:
        return
    if start == end:
        arr[index] = val
        tree[node] = val
        return
    update(arr, tree, node*2, start, (start+end)//2, index, val)
    update(arr, tree, node*2+1, (start+end)//2+1, end, index, val)
    tree[node] = (tree[node*2] * tree[node*2+1]) % DIV


n, m, k = map(int, sys.stdin.readline().split())
arr = []
h = math.ceil(math.log2(n))
tree_size = 1 << (h+1)
tree = [0] * tree_size

for _ in range(n):
    arr.append(int(sys.stdin.readline()))

init(arr, tree, 1, 0, n-1)

for i in range(m+k):
    a, b, c = map(int, sys.stdin.readline().split())

    if a == 1:
        index, val = b, c
        update(arr, tree, 1, 0, n - 1, index - 1, val)
    else:
        left, right = b, c
        print(query(tree, 1, 0, n-1, left-1, right-1))
