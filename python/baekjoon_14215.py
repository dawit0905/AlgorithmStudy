def max_triangle_perimeter(a, b, c):
    # 막대 길이를 정렬하여 a <= b <= c로 만듦
    a, b, c = sorted([a, b, c])

    # 삼각형의 부등식을 만족하도록 c를 조정
    if a + b > c:
        return a + b + c  # 이미 조건을 만족하면 그대로 둘레 반환
    else:
        c = a + b - 1  # c를 조정하여 삼각형 조건을 만족시킴
        return a + b + c  # 새로운 둘레 반환


# 입력 받기
a, b, c = map(int, input().split())

# 결과 출력
print(max_triangle_perimeter(a, b, c))
