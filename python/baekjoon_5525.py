import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
string = sys.stdin.readline().rstrip()

i = 0
pattern = 0
answer = 0
while i < m - 2:

    if string[i:i + 3] == 'IOI':
        pattern += 1
        if pattern == n:
            answer += 1
            pattern -= 1
        i += 2
    else:
        pattern = 0
        i += 1
print(answer)
