import sys


def recursion(s, l, r):
    global cnt
    cnt += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l+1, r-1)


def is_palindrome(s):
    return recursion(s, 0, len(s)-1)


tc = int(sys.stdin.readline())

for t in range(tc):
    cnt = 0
    s = sys.stdin.readline().strip()
    print(is_palindrome(s), cnt)

