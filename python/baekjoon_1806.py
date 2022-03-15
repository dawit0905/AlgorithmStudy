import sys

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

sum_arr = [0] * (n+1)
for i in range(1,n+1):
    sum_arr[i] = sum_arr[i-1] + arr[i-1]

start = 0
end = 1
answer = sys.maxsize

while start != n:
    if sum_arr[end] - sum_arr[start] >= s:
        if end - start < answer:
            answer = end-start
        start += 1

    else:
        if end != n:
            end += 1
        else:
            start += 1

if answer != sys.maxsize:
    print(answer)
else:
    print(0)
