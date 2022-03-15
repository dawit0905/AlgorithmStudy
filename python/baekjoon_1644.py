import sys


def prime_list(n):
    arr = [False, False] + [True] * (n-1)

    m = int(n ** 0.5)
    for i in range(2, m+1):
        if arr[i]:
            for j in range(2*i, n+1, i):
                arr[j] = False

    return [i for i in range(2, n+1) if arr[i]]


n = int(sys.stdin.readline())
prime_arr = prime_list(n)

left = 0
right = 0
cnt = 0

while right <= len(prime_arr):
    total = sum(prime_arr[left:right])

    if total == n:
        cnt += 1
        right += 1

    if total < n:
        right += 1
    elif total > n:
        left += 1

print(cnt)
