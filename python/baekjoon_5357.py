import sys


n = int(sys.stdin.readline())

for i in range(n):
    s = sys.stdin.readline().rstrip()
    answer = []
    for j in s:
        if len(answer) == 0:
            answer.append(j)
        elif answer[-1] != j:
            answer.append(j)

    print(*answer, sep="")
