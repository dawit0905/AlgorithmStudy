import sys
import math


n, kim, lim = map(int, sys.stdin.readline().split())

round = 1

while n >= 1:
    if math.ceil(kim / 2) == math.ceil(lim / 2):
        print(round)
        break

    n //= 2
    round += 1

    kim = math.ceil(kim / 2)
    lim = math.ceil(lim / 2)