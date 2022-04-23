import sys
from itertools import combinations

l, c = map(int, sys.stdin.readline().split())
arr = sorted(sys.stdin.readline().rstrip().split())
words = combinations(arr, l)
for word in words:
    flag = 0
    flag2 = 0
    for i in word:
        if i in "aeiou":
            flag2 += 1
        else:
            flag += 1
    if flag >= 2 and flag2 >= 1:
        print(*word, sep="")