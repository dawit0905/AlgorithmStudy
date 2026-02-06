import sys

switch_cnt = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
student_cnt = int(sys.stdin.readline())
for _ in range(student_cnt):
    gender, num = map(int, sys.stdin.readline().split())

    if gender == 1:
        for i in range(num - 1, len(arr), num):
            arr[i] ^= 1
    else:
        arr[num - 1] ^= 1
        left, right = num - 1, num - 1
        while (0 <= left - 1 and right + 1 < len(arr)) and arr[left - 1] == arr[right + 1]:
            arr[left - 1] ^= 1
            arr[right + 1] ^= 1
            left -= 1
            right += 1

for i in range(0, switch_cnt, 20):
    print(*arr[i:i + 20])
