import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(sys.stdin.readline().strip())

command = []

# 1. KBS1 찾기
target_idx = arr.index('KBS1')

# KBS1이 있는 곳까지 화살표 내리기 (1번 명령)
for _ in range(target_idx):
    command.append(1)

# KBS1을 맨 위로 올리기 (4번 명령)
for _ in range(target_idx):
    command.append(4)
    # 배열에서도 실제로 이동시켜야 함 (swap)
    arr[target_idx], arr[target_idx - 1] = arr[target_idx - 1], arr[target_idx]
    target_idx -= 1

# 2. KBS2 찾기
target_idx = arr.index('KBS2')

# KBS2가 있는 곳까지 화살표 내리기 (1번 명령)
for _ in range(target_idx):
    command.append(1)

# KBS2를 두 번째 자리(인덱스 1)로 올리기 (4번 명령)
# 주의: KBS2가 이미 두 번째 자리에 있다면 아무것도 안 함
# target_idx가 1이 될 때까지 올림
for _ in range(target_idx - 1):
    command.append(4)
    # 배열에서도 실제로 이동
    arr[target_idx], arr[target_idx - 1] = arr[target_idx - 1], arr[target_idx]
    target_idx -= 1

print(*command, sep='')
