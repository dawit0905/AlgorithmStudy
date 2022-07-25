import sys

n = int(sys.stdin.readline())
arr = []
result = ''
for _ in range(n):
    _str = sys.stdin.readline().rstrip()
    arr.append(_str)

for i in range(len(arr[0])):
    text = arr[0][i]
    flag = True
    for j in range(n):
        if text != arr[j][i]:
            flag = False

    if flag:
        result += arr[0][i]
    else:
        result += '?'

print(result)