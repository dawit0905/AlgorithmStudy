import sys

n = sys.stdin.readline().rstrip()

if '0' not in n:
    print(-1)
else:
    total = 0
    for i in range(len(n)):
        total += int(n[i])

    if total % 3 != 0:
        print(-1)
    else:
        sorted_number = sorted(n, reverse=True)
        answer = "".join(sorted_number)
        print(answer)