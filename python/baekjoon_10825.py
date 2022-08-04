import sys

# 이름, 국어, 영어, 수학
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(str, sys.stdin.readline().split())))

arr = sorted(arr, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in arr:
    print(i[0])