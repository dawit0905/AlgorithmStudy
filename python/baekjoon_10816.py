import sys

n = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().split()))
n_arr.sort()

m = int(sys.stdin.readline())
m_arr = list(map(int, sys.stdin.readline().split()))

answer = [0] * m

for i in range(m):
    start = 0
    end = n-1

    while start <= end:
        mid = (start+end) // 2

        if n_arr[mid] == m_arr[i]:
            answer[i] = n_arr[start:end+1].count(m_arr[i])
            break
        elif n_arr[mid] >= m_arr[i]:
            end = mid - 1
        else:
            start = mid + 1

print(*answer)



