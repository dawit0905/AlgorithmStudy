import sys


n = int(sys.stdin.readline())

for i in range(n):
    num, s = sys.stdin.readline().strip().split()
    num = int(num)

    s = s[:num-1] + s[num:]
    print(s)
