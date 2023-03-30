import sys


a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

write_cnt = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

s = []
for i in range(len(a)):
    s.append(write_cnt[ord(a[i]) - 65])
    s.append(write_cnt[ord(b[i]) - 65])


while len(s) > 2:
    tmp = []
    for i in range(len(s)-1):
        tmp.append((int(s[i]) + int(s[i+1])) % 10)
    s = tmp

print(*s, sep='')
