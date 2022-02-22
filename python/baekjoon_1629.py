'''
참고한 블로그
https://velog.io/@grace0st/%EA%B3%B1%EC%85%88-%EB%B0%B1%EC%A4%80-1629%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC
a = 10 , b = 11 , c = 12
10^11 % 12
= ((10^5)%12 x (10^5)%12 x 10)% 12
= ((10^2)%12 x (10^2)%12 x 10) %12 x (10^2)%12 x (10^2)%12 x 10) %12 x 10) %12

4번의 dnc을 호출하게 되면서
(4+4+4+4)%12 = 4가 나오게된다.
'''

a, b, c = map(int, input().split(' '))


def dnc(length):
    if length == 1:
        return a % c
    if length % 2 == 0:
        left = dnc(length // 2)
        return left * left % c
    else:
        left = dnc(length // 2)
        return left * left * a % c


print(dnc(b))