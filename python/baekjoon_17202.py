import sys


a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

s = ''

for i in range(len(a)):
    s += a[i]
    s += b[i]

while len(s) > 2:
    tmp = ''
    for i in range(1, len(s), 1):
        tmp += str((int(s[i-1]) + int(s[i]))%10)
    s = tmp

print(s)
