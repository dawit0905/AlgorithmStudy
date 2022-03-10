import sys

string = sys.stdin.readline().rstrip()
stack = []
idx = 0
answer = 0
while len(string) > idx:
    if string[idx] == '(' and string[idx+1] == ')':
        answer += len(stack)
        idx += 2
    elif string[idx] == '(':
        stack.append('(')
        answer += 1
        idx += 1
    elif string[idx] == ')':
        stack.pop(-1)
        idx += 1

print(answer)

