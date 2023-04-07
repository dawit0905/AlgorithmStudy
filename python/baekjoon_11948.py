import sys


arr = []
arr2 = []
for i in range(4):
    arr.append(int(sys.stdin.readline()))

for i in range(2):
    arr2.append(int(sys.stdin.readline()))

arr.sort()
arr2.sort()

print(arr[3]+arr[2]+arr[1]+arr2[1])

