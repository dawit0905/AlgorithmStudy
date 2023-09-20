import sys


n = int(sys.stdin.readline())

arr = [int(sys.stdin.readline()) for i in range(n)]
reverse_arr = arr[::-1]
cnt = 0
for i in range(0, n-1):
    if reverse_arr[i] <= reverse_arr[i+1]:
        num = reverse_arr[i+1]
        reverse_arr[i+1] = reverse_arr[i] - 1
        cnt += num - reverse_arr[i+1]

print(cnt)
