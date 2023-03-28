import sys


s = sys.stdin.readline().strip()

flag = 0
idx = 0
tmp = []
answer = ''
while idx < len(s):
    if s[idx] == '<':
        if len(tmp):
            answer += ''.join(tmp[::-1])
            tmp = []
        flag = 1
        tmp.append(s[idx])
    elif s[idx] == '>':
        tmp.append('>')
        answer += ''.join(tmp)
        tmp = []
        flag = 0
    elif flag:
        tmp.append(s[idx])
        idx += 1
        continue
    elif s[idx] == ' ':
        answer += ''.join(tmp[::-1]) + ' '
        tmp = []
    else:
        tmp.append(s[idx])

    if idx == len(s)-1:
        answer += ''.join(tmp[::-1])
    idx += 1

print(answer)
