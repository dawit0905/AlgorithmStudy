import sys


n = int(sys.stdin.readline())
arr = sys.stdin.readline().rstrip()
num_dict = {}
num = [int(sys.stdin.readline()) for i in range(n)]

index = 0
for i in arr:
    if i.isalpha() and i not in num_dict:
        num_dict[i] = num[index]
        index += 1


stack = []

for i in arr:
    if i.isalpha():
        num = num_dict[i]
        stack.append(num)
    else:
        b = stack.pop(-1)
        a = stack.pop(-1)

        if i == '+':
            result = a + b
        elif i == '-':
            result = a - b
        elif i == '*':
            result = a * b
        elif i == '/':
            result = a / b

        stack.append(result)

print(f"{stack[0]:.2f}")

