import sys
from collections import deque

n = int(sys.stdin.readline())
papers = list(map(int, sys.stdin.readline().split()))

ballonns = deque(enumerate(papers, start=1))

result = []

while ballonns:
    idx, move = ballonns.popleft()
    result.append(idx)

    if not ballonns:
        break

    if move > 0:
        ballonns.rotate(-(move - 1))
    else:
        ballonns.rotate(-move)

print(*result)
