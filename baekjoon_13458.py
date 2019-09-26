'''
N -> 시험장 개수
A -> N번재 시험장에 있는 응시자수
A(i) -> 각 시험장에 있는 응시자 수
B -> 총감독관이 감시할 수 있는 응시생 수
C -> 부감독관이 감시할 수 있는 응시생 수
시험자에 총감독관은 1명만 있어야된다. 부감독관은 여러명 있어도됨.
필요한 감독관의 수를 구하여라.

A
A(i)
B C

'''

import sys

N = int(sys.stdin.readline())
list_A = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split(" "))

ans = 0
for i in range(N):
    if list_A[i] > 0:
        list_A[i] -= B
        ans += 1

    if list_A[i] > 0:
        ans += int(list_A[i] / C)
        if list_A[i] % C != 0:
            ans += 1

print(ans)

