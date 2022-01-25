import sys

n = int(sys.stdin.readline())

array = []

for i in range(n):
    array.append(list(sys.stdin.readline().split()))
    array[i][0] = int(array[i][0])
    array[i].append(i)

array = sorted(array, key= lambda x: (x[0], x[2]))


for i in array:
    print(i[0],i[1])
