import sys


tc = int(sys.stdin.readline())

for t in range(tc):
    S, L = [], []

    N = int(sys.stdin.readline())

    for n in range(N):
        tmp = list(sys.stdin.readline().split())
        S.append(tmp[0])
        L.append(int(tmp[1]))

    answer_index = 0
    for i, l in enumerate(L):
        if L[answer_index] < l:
            answer_index = i

    print(S[answer_index])
