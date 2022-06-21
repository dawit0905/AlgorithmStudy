import sys


def solution():
    for j in range(len(arr)-1):
        if arr[j] in arr[j+1][0:len(arr[j])]:
            return False
    return True


t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    arr = []
    for j in range(n):
        arr.append(sys.stdin.readline().rstrip())

    arr.sort()
    if solution():
        print('YES')
    else:
        print('NO')

