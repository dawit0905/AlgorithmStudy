import sys


while True:
    a = int(sys.stdin.readline())
    if a == 0:
        break

    for i in range(1, a+1):
        print(i*'*')

