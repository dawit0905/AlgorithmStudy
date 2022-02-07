import sys

n = int(sys.stdin.readline())

listA = list(map(int, sys.stdin.readline().split()))
listB = list(map(int, sys.stdin.readline().split()))
listA.sort()
listB.sort(reverse=True)

total = 0
for i in range(n):
    total = total + listA[i]*listB[i]
print(total)