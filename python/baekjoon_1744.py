import sys


N = int(sys.stdin.readline())
positive = []
negative = []
result = 0

for _ in range(N):
    n = int(sys.stdin.readline())

    if n > 1:
        positive.append(n)
    elif n == 1:
        result += 1
    else:
        negative.append(n)

positive.sort(reverse=True)  # 양수의 큰 수부터 정렬한다.
negative.sort()  # 음수의 작은 수부터 정렬한다.

# 양수
if len(positive) % 2 == 0:
    for i in range(0, len(positive), 2):
        result += positive[i] * positive[i + 1]
else:
    for i in range(0, len(positive) - 1, 2):
        result += positive[i] * positive[i + 1]
    result += positive[len(positive) - 1]

# 음수
if len(negative) % 2 == 0:
    for i in range(0, len(negative), 2):
        result += negative[i] * negative[i + 1]
else:
    for i in range(0, len(negative) - 1, 2):
        result += negative[i] * negative[i + 1]
    result += negative[len(negative) - 1]

print(result)