import sys

n = int(sys.stdin.readline())
array = []
for _ in range(n):
    array.append(list(map(int, sys.stdin.readline().split())))

array.sort()

for i in array:
    print(i[0],i[1])