import sys


a, b, c, d = map(int, sys.stdin.readline().split())

answer = sys.maxsize

answer = min(answer, abs((a+b) - (c+d)))
answer = min(answer, abs((a+c) - (b+d)))
answer = min(answer, abs((a+d) - (b+c)))

print(answer)