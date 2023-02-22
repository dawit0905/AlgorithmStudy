import sys


cnt = 1
while True:
    n, *arr = map(int, sys.stdin.readline().split())
    if n == 0:
        break
    arr = list(arr)
    if n % 2 == 1:
        ans = arr[n//2] * 10
    else:
        ans = (arr[n//2-1] + arr[n//2]) * 5



    print(f'Case {cnt}: {ans/10}')
    cnt += 1