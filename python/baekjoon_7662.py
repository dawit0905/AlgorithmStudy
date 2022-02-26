import sys
from heapq import heappop, heappush

k = int(sys.stdin.readline())

for i in range(k):
    n = int(sys.stdin.readline())
    min_arr = []
    max_arr = []
    dict = {}
    for j in range(n):
        cmd, num = map(str, sys.stdin.readline().split())
        num = int(num)
        if cmd == 'I':
            heappush(min_arr, num)
            heappush(max_arr,-num)
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
        else:
            if num == 1:
                while max_arr:
                    temp = -heappop(max_arr)
                    if dict[temp] > 0:
                        dict[temp] -= 1
                        break
            else:
                while min_arr:
                    temp = heappop(min_arr)
                    if dict[temp] > 0:
                        dict[temp] -= 1
                        break

    result = []
    for key, value in dict.items():
        if value > 0:
            result.append(key)

    if len(result) > 0:
        result.sort()
        print(result[-1], result[0])
    else:
        print('EMPTY')