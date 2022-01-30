'''
시간 초과 발생!
import sys
n = int(sys.stdin.readline())

array = list(map(int,sys.stdin.readline().split()))
answer = []
for i in range(len(array)):
    for j in range(i,len(array)):
        flag = 0
        if i == len(array) and j == len(array):
            break
        if array[i] < array[j] :
            flag = 1
            answer.append(array[j])
            break
    if flag == 0:
        answer.append(-1)

for i in answer:
    print(i, end=" ")
'''

import sys
n = int(input())
A = list(map(int, sys.stdin.readline().split()))
answer = [-1] * n
stack = [0]

for i in range(1, n):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)

print(*answer)


