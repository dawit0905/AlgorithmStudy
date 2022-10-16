import sys


def REV(s) -> int:
    result = 0
    exp = 10 ** (len(s)-1)
    for i in s[::-1]:
        result += int(i)*exp
        exp //= 10

    return result


a, b = map(str, sys.stdin.readline().split())
print(REV(str(REV(a) + REV(b))))
