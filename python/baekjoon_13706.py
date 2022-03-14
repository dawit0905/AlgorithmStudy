n = int(input())
start = 1
end = n

while 1:
    mid = (start+end) // 2

    if n == mid**2:
        print(mid)
        break

    if mid**2 < n:
        start = mid + 1

    if mid**2 > n:
        end = mid - 1