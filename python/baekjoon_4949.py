import sys


while 1:
    # 데이터 입력
    input_data = sys.stdin.readline().rstrip()
    # 종료 조건
    if input_data == '.':
        break
    # 괄호 합계
    parenthesis_sum = 0
    square_brackets_sum = 0
    # 괄호를 담을 배열
    array = []
    # 현재값이 ) 이거나 ] 일때 array에서 꺼낸 값(바로 앞에 있는 괄호가 [ or ( 이면 no을 하기 위한 변수
    temp = ''

    for i in input_data:
        if i == '(' :
            parenthesis_sum += 1
            array.append('(')
        elif i == ')':
            parenthesis_sum -= 1
            if parenthesis_sum < 0 :
                break
            temp = array.pop()
        elif i == '[' :
            square_brackets_sum += 1
            array.append('[')
        elif i == ']':
            square_brackets_sum -= 1
            if square_brackets_sum < 0:
                break
            temp = array.pop()

        if len(array) > 0:
            if temp == '(' and i == ']':
                break
            elif temp == '[' and i == ')':
                break

    if parenthesis_sum == 0 and square_brackets_sum == 0:
        print('yes')
    else:
        print('no')
