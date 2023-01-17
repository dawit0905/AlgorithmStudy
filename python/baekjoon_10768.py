import sys


a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

if a == 2 and b == 18:
    print('Special')
elif a > 2:
    print('After')
elif a == 2 and b < 18:
    print('Before')
elif a < 2:
    print('Before')
else:
    print('After')
