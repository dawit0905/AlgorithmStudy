import sys

t = int(sys.stdin.readline())

for i in range(t):
    passwd = sys.stdin.readline().rstrip()
    s1 = []
    s2 = []

    for j in passwd:
        if j == '<' and len(s1) >= 1:
            s2.append(s1.pop(-1))
        elif j == '>' and len(s2) >= 1:
            s1.append(s2.pop(-1))
        elif j == '-' and len(s1) >= 1:
            s1.pop(-1)
        elif j.isdigit() or j.isalpha():
            s1.append(j)

    s2.reverse()
    print(*(s1+s2), sep='')
