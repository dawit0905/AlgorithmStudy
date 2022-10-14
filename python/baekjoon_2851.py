import sys


arr = [0]
for i in range(10):
    arr.append(int(sys.stdin.readline()))

s = [0] * 11
answer = 0
for i in range(1, 11):
    s[i] = s[i-1] + arr[i]

    if abs(answer - 100) >= abs(s[i] - 100):
        if s[i] > answer:
            answer = s[i]


print(answer)