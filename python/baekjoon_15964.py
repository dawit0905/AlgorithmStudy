import sys


A, B = map(int, sys.stdin.readline().split())
print(eval('(A+B)*(A-B)'))
