import sys


while True:
    s = sys.stdin.readline().rstrip()
    if s == 'END':
        break
    for i in s[::-1]:
        print(i, end="")
    print()
