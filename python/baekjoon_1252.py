import sys


a, b = sys.stdin.readline().strip().split()

print(bin(int(a, 2)+int(b,2))[2:])