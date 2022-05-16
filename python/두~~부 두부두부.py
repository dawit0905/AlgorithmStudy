import sys

n, m, k = map(int, sys.stdin.readline().split())
mo = 3
# mo = 3
# n = 7
# m = 2
# k = 4
while True:

    if mo == k:
        print(m)
        break
    elif mo < k:
        if m == n:
            m = 1
        else:
            m = m+1
        mo += 1
    elif mo > k:
        if m == 1:
            m=n
        else:
            m = m - 1
        mo -= 1