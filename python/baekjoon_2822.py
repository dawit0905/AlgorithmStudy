import sys
import copy

arr = []
for i in range(8):
    arr.append(int(sys.stdin.readline()))

tmp = copy.deepcopy(arr)
tmp.sort()
answer = []
_sum = 0
for i in range(5):
    idx = arr.index(tmp.pop(-1))
    answer.append(idx+1)
    _sum += arr[idx]
    arr[idx] = -1


answer.sort()
print(_sum)
print(*answer)
