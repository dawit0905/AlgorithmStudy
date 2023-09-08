import sys


def find_prime():
    prime_flag = [1] * 1004000
    prime_flag[1] = 0
    prime_flag[2] = 1
    for i in range(2, 1004000):
        if prime_flag[i]:
            for j in range(i+i, 1004000, i):
                prime_flag[j] = 0

    return prime_flag


def isPalidrome(s):
    for i in range(0, len(s)//2):
        if s[i] != s[len(s)-i-1]:
            break
    else:
        return True

    return False


n = int(sys.stdin.readline())
prime_flag = find_prime()

for i in range(n, 1004000):
    if prime_flag[i] and isPalidrome(str(i)):
        print(i)
        break