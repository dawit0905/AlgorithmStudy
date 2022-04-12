import sys

'''
n이 어마어마하게 크지만 우리는 제곱수를 O(logn)의 시간에 구할 수 있다.
(분할정복 1629 곱셈 www.acmicpc.net/problem/1629)

따라서 [[1,1],[1,0]]의 n-2승 값을 먼저 구해준 후 초기값 1,1과 행렬의 곱셈을 해준다면 쉽게 구할 수 있다.
행렬의 곱셈을 할 때 모듈러 연산은 곱셈,덧셈,뺄셈에 대해서 분배법칙이 성립하므로 덧셈한걸 나눈 값으로 넣어준다.
'''


#제곱을 구하는 분할정복
def power(adj,n):
    if n==1:
        return adj
    elif n%2:
        return multi(power(adj,n-1),adj)
    else:
        return power(multi(adj,adj),n//2)


#행렬의 곱셈
def multi(a,b):
    temp=[[0]*len(b[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            sum=0
            for k in range(2):
                sum+=a[i][k]*b[k][j]
            temp[i][j]=sum%mod
    return temp


#초기 행렬
mod=1000000007
adj=[[1,1],[1,0]]
#피보나치 초기값
start=[[1],[1]]
n=int(sys.stdin.readline())
if n<3:
    print(1)
else:
    print(multi(power(adj,n-2),start)[0][0])