import sys

while True:
    try:
        s = sys.stdin.readline().rstrip('\n')

        if not s:
            break

        # 소문자, 대문자, 숫자, 공백
        arr = [0, 0, 0, 0]
        for t in s:
            if 97 <= ord(t) <= 122:
                arr[0] += 1
            elif 65 <= ord(t) <= 90:
                arr[1] += 1
            elif t.isalnum():
                arr[2] += 1
            elif t == ' ':
                arr[3] += 1
        print(*arr)
    except EOFError:
        break