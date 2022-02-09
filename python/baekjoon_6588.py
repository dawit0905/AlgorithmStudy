# # 골드바흐의 추측
import sys
MAX = 1000000
ans = [False, False] + [True]*(MAX-1)
primes = []

for i in range(2, MAX+1):
    if ans :
        primes.append(i)
        for j in range(i*2,MAX+1,i):
            ans[j] = False

while True:
    flag = False
    number = int(sys.stdin.readline())
    if number == 0:
        break
    for i in range(2,number):
        if ans[i] and ans[number-i]:
            print("{} = {} + {}".format(number,i,number-i))
            flag = True
            break
    if not flag:
        print("Goldbach's conjecture is wrong.")


# import sys
# input = sys.stdin.readline
#
# a = [0, 0] + [1]*(1000001-1)
# for i in range(2, 1001):
#     for j in range(2*i, 1000001+1, i):
#         a[j] = 0
#
# def solve(n):
#     for num in range(2, n):
#         if a[num] and a[n-num]:
#             print(n, "=", num, "+", n-num)
#             return
#     print("Goldbach's conjecture is wrong.")
#     return
#
# while True:
#     n = int(input())
#     if not n:
#         break
#     solve(n)