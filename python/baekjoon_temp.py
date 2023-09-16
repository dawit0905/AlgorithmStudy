import sys


w, h = map(int, sys.stdin.readline().split())
print(round(w*h*0.5, 1))