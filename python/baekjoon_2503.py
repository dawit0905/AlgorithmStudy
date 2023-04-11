from itertools import permutations
import sys


num = list(permutations(range(1, 10), 3))
t = int(sys.stdin.readline())
for _ in range(t):
    q, strike, ball = map(int, sys.stdin.readline().split())
    removed = 0
    q = list(str(q))

    for i in range(len(num)):
        strike_cnt, ball_cnt = 0, 0
        i -= removed
        for j in range(3):
            q[j] = int(q[j])
            if q[j] in num[i]:
                if j == num[i].index(q[j]):
                    strike_cnt += 1
                else:
                    ball_cnt += 1

        if strike_cnt != strike or ball_cnt != ball:
            num.remove(num[i])
            removed += 1

print(len(num))