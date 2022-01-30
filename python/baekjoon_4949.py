import sys


while 1:
    input_data = sys.stdin.readline().rstrip()
    array = []
    # 종료 조건
    if input_data == '.':
        break
    # 괄호 합계
    parenthesis_sum = 0
    square_brackets_sum = 0

    # 특이 케이스 처리
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
    else :
        print('no')
