import sys

a, b = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())

minite = (b+c)%60
hour = (a+(b+c)//60) % 24

print(hour, minite)