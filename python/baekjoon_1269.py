import sys


n, m = map(int, sys.stdin.readline().split())
A = set(list(map(int, sys.stdin.readline().split())))
B = set(list(map(int, sys.stdin.readline().split())))

print(len(A-B)+len(B-A))


