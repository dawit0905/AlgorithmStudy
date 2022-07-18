import sys


_str = sys.stdin.readline().rstrip()
bomb_str = sys.stdin.readline().rstrip()
stack = []

for s in _str:
    stack.append(s)
    if bomb_str[-1] == s and ''.join(stack[-len(bomb_str):]) == bomb_str:
        del stack[-len(bomb_str):]

answer = ''.join(stack)

if answer == '':
    print('FRULA')
else:
    print(answer)
