import math


def solution(n, sqrt_num):
    for i in range(sqrt_num):
        for j in range(sqrt_num):
            for k in range(sqrt_num):
                for t in range(sqrt_num):
                    if n == t ** 2:
                        answer = 1
                        return answer
                    if n == t ** 2 + k ** 2:
                        answer = 2
                        return answer
                    if n == t ** 2 + k ** 2 + j ** 2:
                        answer = 3
                        return answer
                    if n == i ** 2 + j ** 2 + k ** 2 + t ** 2:
                        answer = 4
                        return answer


n = int(input())
sqrt_num = int(math.sqrt(n)) + 1

print(solution(n, sqrt_num))
