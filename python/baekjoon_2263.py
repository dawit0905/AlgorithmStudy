import sys


def solution(iStart, iEnd, pStart, pEnd):
    if(iStart > iEnd) or (pStart > pEnd):
        return
    parent = postorder[pEnd]
    preorder.append(parent)
    left = index[parent] - iStart
    right = iEnd -index[parent]

    solution(iStart, iStart + left - 1, pStart, pStart + left - 1)
    solution(iEnd - right + 1, iEnd, pEnd - right, pEnd - 1)


sys.setrecursionlimit(int(1e9))
n = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))
preorder = []
index = [0] * (n+1)
for i in range(n):
    index[inorder[i]] = i

solution(0, n-1, 0, n-1)
print(*preorder)