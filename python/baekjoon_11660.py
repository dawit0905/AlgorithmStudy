# 참고 블로그
# https://velog.io/@ready2start/Python-%EB%B0%B1%EC%A4%80-11660-%EA%B5%AC%EA%B0%84-%ED%95%A9-%EA%B5%AC%ED%95%98%EA%B8%B0-5
from sys import stdin


n, m = map(int, stdin.readline().split())

numbers = [[0] * (n + 1)]

for _ in range(n):
    nums = [0] + [int(x) for x in stdin.readline().split()]
    numbers.append(nums)

# prefix sum 행렬 만들기

# 1. 행 별로 더하기
for i in range(1, n + 1):
    for j in range(1, n):
        numbers[i][j + 1] += numbers[i][j]

# 2. 열 별로 더하기
for j in range(1, n + 1):
    for i in range(1, n):
        numbers[i + 1][j] += numbers[i][j]

# for i in numbers:
#     print(*i)

for _ in range(m):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    # (x1, y1)에서 (x2, y2)까지의 합
    # p[x2][y2] - p[x1 - 1][y2] - p[x2][y1 - 1] + p[x1 - 1][y1 - 1]
    print(numbers[x2][y2] - numbers[x1 - 1][y2] - numbers[x2][y1 - 1] + numbers[x1 - 1][y1 - 1])