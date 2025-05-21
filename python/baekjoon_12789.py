import sys

n = int(sys.stdin.readline())
stack1 = list(map(int, sys.stdin.readline().split()))
stack2 = []
now = 1

while stack1:
    if stack1[0] == now:
        stack1.pop(0)
        now += 1
    elif stack2 and stack2[-1] == now:
        stack2.pop()
        now +=1
    else:
        stack2.append(stack1.pop(0))

for i in stack2[::-1]:
    if i == now:
        stack2.pop()
        now += 1
    else:
        print('Sad')
        exit(0)

print('Nice')
