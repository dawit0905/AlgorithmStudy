def solution():
    count = 0
    for i in range(1, len(arr) + 1):
        if arr[i - 1] == i:
            count += 1
    if count == 8:
        return 'ascending'

    count = 0
    for i in range(8, 0, -1):
        if arr[len(arr)-i] == i:
            count += 1
    if count == 8:
        return 'descending'

    return 'mixed'


arr = list(map(int, input().split()))
print(solution())
