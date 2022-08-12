import sys


def move(gear_index, direction) -> list:
    result = [-1] * 8
    if direction == 1:
        for i in range(8):
            result[i] = gear_wheel[gear_index][i-1]
    else:
        for i in range(8):
            result[i] = gear_wheel[gear_index][(i+1)%8]
    return result


gear_wheel = []
for i in range(4):
    gear_wheel.append(list(map(int, list(sys.stdin.readline().rstrip()))))

k = int(sys.stdin.readline())
for i in range(k):
    target, direction = map(int, sys.stdin.readline().split())
    target -= 1

    # 백업
    tmp_2 = gear_wheel[target][2]  # 비교 대상 백업
    tmp_6 = gear_wheel[target][6]  # 비교 대상 백업
    # 자신 돌리기
    gear_wheel[target] = move(target, direction)


    direct = direction
    for i in range(target - 1, -1, -1):
        if gear_wheel[i][2] != tmp_6:  # 서로 다른 극인 경우
            tmp_6 = gear_wheel[i][6]
            gear_wheel[i] = move(i, -direct)
            direct *= -1
        else:
            break


    # 시작 톱니 오른쪽 방향
    direct = direction
    for i in range(target+1,4):
        if gear_wheel[i][6] != tmp_2:		# 서로 다른 극인 경우
            tmp_2 = gear_wheel[i][2]
            gear_wheel[i] = move(i, -direct)
            direct *= -1
        else:
            break

    # # 왼쪽
    # if target-1 >= 0 and gear_wheel[target][6] != gear_wheel[target-1][2]:
    #     temp = gear_wheel[target-1]
    #     gear_wheel[target-1] = move(target - 1, direction * -1)
    #     if target - 2 >= 0 and gear_wheel[target-1][6] != gear_wheel[target - 2][2]:
    #         temp = gear_wheel[target-2]
    #         gear_wheel[target-2] = move(target - 2, direction)
    #         if target - 3 >= 0 and gear_wheel[target-2][6] != gear_wheel[target - 3][2]:
    #             gear_wheel[target - 3] = move(target - 3, direction * -1)
    # # 오른쪽
    # if target+1 <= 3 and gear_wheel[target][2] != gear_wheel[target+1][6]:
    #     temp = gear_wheel[target + 1]
    #     gear_wheel[target+1] = move(target + 1, direction * -1)
    #     if target + 2 <= 3 and gear_wheel[target+1][2] != gear_wheel[target + 2][6]:
    #         temp = gear_wheel[target + 2]
    #         gear_wheel[target+2] = move(target + 2, direction)
    #         if target + 3 <= 3 and gear_wheel[target+2][2] != gear_wheel[target + 3][6]:
    #             gear_wheel[target + 3] = move(target + 3, direction * -1)



result = 0
adder = [1, 2, 4, 8]
for i in range(4):
    if gear_wheel[i][0] == 1:
        result += adder[i]

# for i in gear_wheel:
#     print(*i)

# print(gear_wheel)
print(result)
