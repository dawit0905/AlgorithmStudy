import sys

n = int(sys.stdin.readline())

if n % 5 == 0 or n % 5 == 2:
    print('CY')
else:
    print('SK')