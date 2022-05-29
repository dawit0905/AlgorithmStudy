import sys

t = int(sys.stdin.readline())

for i in range(t):
    passwd = sys.stdin.readline().rstrip()
    answer = []
    pointer = 0
    index = 0
    while pointer <= len(passwd)-1:
        if passwd[pointer] == '-' and len(answer) >= 1:
            answer.pop(-1)
        elif passwd[pointer] == '<' and index > 0:
            index -= 1
        elif passwd[pointer] == '>':
            index += 1
        elif passwd[pointer].isalpha() or passwd[pointer].isdigit():
            answer.insert(index, passwd[pointer])
            index += 1

        pointer += 1

    print(*answer, sep='')

