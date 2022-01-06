import sys
n = sys.stdin.readline().rstrip()
sum = 0
length = len(n) -1

def casting(n):
    if n == 'A':
        return 10
    elif n == 'B':
        return 11
    elif n == 'C':
        return 12
    elif n == 'D':
        return 13
    elif n == 'E':
        return 14
    elif n == 'F':
        return 15
    else : return n

for i in range(len(n)):
    sum += int(casting(n[i])) * 16 ** length
    length -= 1

print(sum)