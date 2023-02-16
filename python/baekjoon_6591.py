import sys


while True:
    n, k = map(int, sys.stdin.readline().split())

    if n == 0 and k == 0:
        break

    nk = n-k
    a = 1
    b = 1

    for i in range(n, max(k, nk), -1):
        a *= i

    for i in range(1, min(k, nk)+1, 1):
        b *= i

    print(a//b)


'''
example: 49 6 
49*48*47*46*45*44 / 6*5*4*3*2*1
'''