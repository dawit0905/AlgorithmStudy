import sys


def ccw(p1, p2, p3):
    return (p1[0]*p2[1]+p2[0]*p3[1]+p3[0]*p1[1]) - (p2[0]*p1[1]+p3[0]*p2[1]+p1[0]*p3[1])


p = []
for i in range(3):
    p.append((list(map(int, sys.stdin.readline().split()))))

ans = ccw(p[0],p[1],p[2])

if ans > 0:
    print(1)
elif ans == 0:
    print(0)
else:
    print(-1)
