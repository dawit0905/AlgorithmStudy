def men_of_passion(n):
    # 수행 횟수 계산
    count = n * (n - 1) * (n - 2) // 6
    return count, 3

# 입력 받기
n = int(input())

# 결과 출력
result, degree = men_of_passion(n)
print(result)
print(degree)
