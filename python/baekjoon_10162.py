abc = [300, 60, 10]
arr = [0, 0, 0]
n = int(input())
if n % 10 != 0:
    print(-1)
else:

    arr[0] += n // abc[0]
    n = n % abc[0]

    arr[1] += n // abc[1]
    n = n % abc[1]

    arr[2] += n // abc[2]
    n = n % abc[2]
    print(*arr)
