# 참조할 블로그 https://at0z.tistory.com/28
# nCr = n-1Cr-1 + n-1Cr 이다.

def binomial_coefficient(n,r):
    if n == r or r == 0:
        return 1
    return binomial_coefficient(n-1,r-1) + binomial_coefficient(n-1,r)


n, k = map(int, input().split())
print(binomial_coefficient(n,k))
