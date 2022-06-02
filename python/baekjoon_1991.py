# import sys
#
# N = int(sys.stdin.readline().strip())
# tree = {}
#
# for n in range(N):
#     root, left, right = sys.stdin.readline().strip().split()
#     tree[root] = [left, right]
#
#
# def preorder(root):
#     if root != '.':
#         print(root, end='')  # root
#         preorder(tree[root][0])  # left
#         preorder(tree[root][1])  # right
#
#
# def inorder(root):
#     if root != '.':
#         inorder(tree[root][0])  # left
#         print(root, end='')  # root
#         inorder(tree[root][1])  # right
#
#
# def postorder(root):
#     if root != '.':
#         postorder(tree[root][0])  # left
#         postorder(tree[root][1])  # right
#         print(root, end='')  # root
#
#
# preorder('A')
# print()
# inorder('A')
# print()
# postorder('A')
'''
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
'''


import sys


def preorder(start):
    if start != -1:
        print(chr(start+65), end='')
        preorder(tree[start][0])
        preorder(tree[start][1])


def inorder(start):
    if start != -1:
        inorder(tree[start][0])
        print(chr(start + 65), end='')
        inorder(tree[start][1])


def postorder(start):
    if start != -1:
        postorder(tree[start][0])
        postorder(tree[start][1])
        print(chr(start + 65), end='')


n = int(sys.stdin.readline())
tree = [[] for _ in range(26)]

for i in range(n):
    temp = list(map(str, sys.stdin.readline().rsplit()))
    a = temp[1]
    b = temp[2]
    if temp[1] == '.':
        a = -1
    else:
        a = ord(a) - 65
    if temp[2] == '.':
        b = -1
    else:
        b = ord(b) - 65
    tree[ord(temp[0])-65] = [a, b]

# print(tree)

preorder(0)
print()
inorder(0)
print()
postorder(0)



