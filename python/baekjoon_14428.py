import sys
import math


def init(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        init(arr, tree, node*2, start, (start+end)//2)
        init(arr, tree, node*2+1, (start+end)//2+1, end)
        if tree[node*2][0] > tree[node*2+1][0]:
            tree[node] = tree[node*2+1]
        else:
            tree[node] = tree[node*2]


def query(arr, tree, node, start, end, left, right):
    if left > end or right < start:
        return [sys.maxsize, sys.maxsize]
    if left <= start and end <= right:
        return tree[node]
    lmin = query(arr, tree, node*2, start, (start+end)//2, left, right)
    rmin = query(arr, tree, node*2+1, (start+end)//2+1, end, left, right)
    if lmin[0] > rmin[0]:
        return rmin
    else:
        return lmin


def update(arr, tree, node, start, end, index, val):
    if index < start or index > end:
        return [sys.maxsize, sys.maxsize]

    if start == end:
        tree[node] = val
        return

    update(arr, tree, node*2, start, (start+end)//2, index, val)
    update(arr, tree, node*2+1, (start+end)//2+1, end, index, val)
    if tree[node*2][0] > tree[node*2+1][0]:
        tree[node] = tree[node * 2 + 1]
    else:
        tree[node] = tree[node * 2]



n = int(sys.stdin.readline())
temp = list(map(int, sys.stdin.readline().split()))
arr = [[0, 0] for i in range(n)]
for i in range(len(temp)):
    arr[i][0] = temp[i]
    arr[i][1] = i+1


m = int(sys.stdin.readline())
h = math.ceil(math.log2(n))
tree_size = 1 << (h+1)
tree = [0] * tree_size
init(arr, tree, 1, 0, n-1)

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())

    if a == 1:
        index, val = b, c
        arr[index-1][0] = c
        update(arr, tree, 1, 0, n-1, index-1, arr[index-1])
    else:
        left, right = b, c
        print(query(arr, tree, 1, 0, n-1, left-1, right-1)[1])

# print(arr)
# print(tree)