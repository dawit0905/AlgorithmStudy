import sys


def combi(number, cnt):
    global result
    if cnt == n:
        checked[result] = 1
        return

    for i in range(number, 4):
        result += arr[i]
        combi(i, cnt+1)
        result -= arr[i]


n = int(sys.stdin.readline())
arr = [1, 5, 10, 50]

result = 0
checked = [0] * (50*20+1)
result_list = []
combi(0, 0)
print(sum(checked))

