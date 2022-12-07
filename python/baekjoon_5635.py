import sys

n = int(sys.stdin.readline())

arr = [[] for _ in range(n)]
for i in range(n):
    tmp = list(sys.stdin.readline().split())
    arr[i].append(tmp[0])
    arr[i].extend(list(map(int, tmp[1:])))

arr.sort(key=lambda x: (x[3], x[2], x[1]))

print(arr[-1][0])
print(arr[0][0])
