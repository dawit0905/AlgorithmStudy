import sys


a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

if a == 60 and b == 60 and c == 60:
    print('Equilateral')
elif a+b+c == 180 and (a == b or a == c or b == c):
    print('Isosceles')
elif a+b+c == 180 and (a != b or a != c or b != c):
    print('Scalene')
else:
    print('Error')