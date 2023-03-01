import sys


ban_word = 'CAMBRIDGE'

s = sys.stdin.readline().strip()
for i in ban_word:
    s = s.replace(i, '')

print(s)
