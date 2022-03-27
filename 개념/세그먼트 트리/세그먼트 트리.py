import sys
import math

'''
5 2 2
1
2
3
4
5
1 3 6
2 2 5
1 5 2
2 3 5
'''

# init은 세그먼트 트리 만드는 함수
# a: 배열 A
# tree: 세그먼트 트리
# node: 노드 번호
# start: 시작 인덱스
# end: 끝 인덱스
def init(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
    else:
        init(a, tree, node*2, start, (start+end)//2)
        init(a, tree, node*2+1, (start+end)//2+1, end)
        tree[node] = tree[node*2] + tree[node*2+1]


# query는 세그먼트 트리에서 [left,right]의 합을 구하는 함수
# a: 배열 A
# tree: 세그먼트 트리
# node: 노드 번호
# start: 시작 인덱스
# end: 끝 인덱스
# left, right: 구간 합을 구하고자 하는 범위
def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    lsum = query(tree, node*2, start, (start+end)//2, left, right)
    rsum = query(tree, node*2+1, (start+end)//2+1, end, left, right)
    return lsum + rsum

# 수 변경하고 변경사항 세그먼트 트리에 적용하기
def update(arr, tree, node, start, end, index, val):
    if index < start or index > end:
        return
    if start == end:
        arr[index] = val
        tree[node] = val
        return
    update(arr, tree, node*2, start, (start+end)//2, index, val)
    update(arr, tree, node*2+1, (start+end)//2+1, end, index, val)
    tree[node] = tree[node*2] + tree[node*2+1]

n, m, k = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]
h = math.ceil(math.log2(n))
tree_size = 1 << (h+1)
tree = [0] * tree_size

init(arr, tree, 1, 0, n-1)

for _ in range(m+k):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        index, val = b, c
        update(arr, tree, 1, 0, n-1, index-1, val)
    else:
        left, right = b, c
        print(query(tree, 1, 0, n-1, left-1, right-1))