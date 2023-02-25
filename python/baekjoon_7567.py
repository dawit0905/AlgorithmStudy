import sys


s = sys.stdin.readline().strip()
total = 10

for i in range(1, len(s)):
    if s[i-1] == s[i]:
        total += 5
    else:
        total += 10

print(total)
