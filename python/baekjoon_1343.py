import sys


s = sys.stdin.readline().strip()

idx = 0
cnt = 0
answer = ''
while idx < len(s):
    now = s[idx]
    if now == '.':
        answer += '.'
        cnt = 0
    elif idx+1 == len(s) or (now == 'X' and now != s[idx+1]):
        num = cnt + 1
        if num % 4 == 0:
            answer += 'AAAA' * (num // 4)

        elif num >= 6 and num % 2 == 0:
            answer += 'AAAA' * (num // 4)
            num = num % 4
            answer += 'BB' * (num // 2)

        elif num % 2 == 0:
            answer += 'BB' * (num//2)

        else:
            print(-1)
            exit(0)
    else:
        cnt += 1
    idx += 1

print(answer)

