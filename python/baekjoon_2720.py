import sys


tc = int(sys.stdin.readline())

for t in range(tc):
    C = int(sys.stdin.readline())
    state = [0] * 4

    if C >= 25:
        state[0] = C // 25
        C = C % 25

    if C >= 10:
        state[1] = C // 10
        C = C % 10

    if C >= 5:
        state[2] = C // 5
        C = C % 5

    if C >= 1:
        state[3] = C // 1
        C = C % 1

    print(*state)