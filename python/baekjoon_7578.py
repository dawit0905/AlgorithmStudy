import sys
'''
132 392 311 351 231
392 351 132 311 231


A 배열을 입력 받는대로
idx를 순서대로 매긴다.
나보다 큰 idx가 있을 경우에, 그 갯수 만큼
B 배열에 같은 원소에 더한다.
'''

def query(tree, node, start, end, left, right):
     if right < start or end < left:
          return 0

     if left <= start and end <= right:
          return tree[node]

     return query(tree, node*2, start, (start+end)//2, left, right) + query(tree, node*2+1, (start+end)//2+1, end, left, right)


def update(tree, node, start, end, index):
     if index < start or end < index:
          return 0

     if start == end:
          tree[node] = 1
          return tree[node]

     update(tree, node*2, start, (start+end)//2, index)
     update(tree, node*2+1, (start+end)//2+1, end, index)
     tree[node] = tree[node*2] + tree[node*2+1]

     return tree[node]


n = int(sys.stdin.readline())
arrA = list(map(str, sys.stdin.readline().split()))
idx = 0

arrB = {}
for num in sys.stdin.readline().split():
     arrB[num] = idx
     idx += 1

h = n * 4
tree = [0] * h
ans = 0

for i in arrA:
     idx = arrB[i]
     ans += query(tree, 1, 0, n-1, idx, n-1)
     update(tree, 1, 0, n-1, idx)

print(ans)
