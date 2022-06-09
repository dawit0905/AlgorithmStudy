import sys

s = int(sys.stdin.readline())
total = 0
index = 0
while total <= s:
    index += 1
    total += index
print(index-1)