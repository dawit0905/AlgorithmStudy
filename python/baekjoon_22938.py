import sys
import math


x1, y1, r1 = map(int, sys.stdin.readline().split())
x2, y2, r2 = map(int, sys.stdin.readline().split())

d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

print("YES") if math.sqrt((r1 + r2)**2) > d else print("NO")


