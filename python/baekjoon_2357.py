import sys
import math
import copy


def min_init(min_array, min_tree, node, start, end):
    if start == end:
        min_tree[node] = min_array[start]
    else:
        min_init(min_array, min_tree, node*2, start, (start+end)//2)
        min_init(min_array, min_tree, node*2+1, (start+end)//2+1, end)
        min_tree[node] = min(min_tree[node*2], min_tree[node*2+1])

def min_query(min_array, min_tree, node, start, end, left, right):
    if left > end or right < start:
        return -1
    elif left <= start and end <= right:
        return min_tree[node]

    lmin = min_query(min_array, min_tree, node*2, start, (start+end)//2, left, right)
    rmin = min_query(min_array, min_tree, node*2+1, (start + end)//2+1, end, left, right)

    if lmin == -1:
        return rmin
    elif rmin == -1:
        return lmin
    else:
        return min(lmin, rmin)


def max_init(max_array, max_tree, node, start, end):
    if start == end:
        max_tree[node] = max_array[start]
    else:
        max_init(max_array, max_tree, node*2, start, (start+end)//2)
        max_init(max_array, max_tree, node*2+1, (start+end)//2+1, end)
        max_tree[node] = max(max_tree[node*2], max_tree[node*2+1])


def max_query(max_array, max_tree, node, start, end, left, right):
    if left > end or right < start:
        return -1
    elif left <= start and end <= right:
        return max_tree[node]

    lmax = max_query(max_array, max_tree, node*2, start, (start+end)//2, left, right)
    rmax = max_query(max_array, max_tree, node*2+1, (start+end)//2+1, end, left, right)

    if lmax == -1:
        return rmax
    elif rmax == -1:
        return lmax
    else:
        return max(lmax, rmax)

n, m = map(int, sys.stdin.readline().split())
min_array = [int(sys.stdin.readline()) for _ in range(n)]
max_array = copy.deepcopy(min_array)
h = math.ceil(math.log2(n))
tree_size = 1 << (h+1)
min_tree = [0] * tree_size
max_tree = [0] * tree_size


min_init(min_array, min_tree, 1, 0, n-1)
max_init(max_array, max_tree, 1, 0, n-1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(min_query(min_array, min_tree, 1, 0, n-1, a-1, b-1), max_query(max_array, max_tree, 1, 0, n-1, a-1, b-1))





