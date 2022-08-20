import sys
import math


def cal(x1, y1, z1, x2, y2, z2) -> float('inf'):
    return ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2) ** (1/2)


ax, ay, az, bx, by, bz, cx, cy, cz = map(int, sys.stdin.readline().split())
ans = 1e9
while 1:
    mx = (ax + bx) / 2
    my = (ay + by) / 2
    mz = (az + bz) / 2
    ac_distance = cal(ax, ay, az, cx, cy, cz)
    bc_distance = cal(bx, by, bz, cx, cy, cz)
    mid_distance = cal(mx, my, mz, cx, cy, cz)

    if abs(ans - mid_distance) <= 1e-6:
        print('%0.10f' % ans)
        break

    if mid_distance < ans:
        ans = mid_distance
    if ac_distance > bc_distance:
        ax, ay, az = mx, my, mz
    else:
        bx, by, bz = mx, my, mz
