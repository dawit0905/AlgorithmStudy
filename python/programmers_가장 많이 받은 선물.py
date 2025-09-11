friends_map = {}
gift_map = [[0] * 51 for _ in range(51)]
point = [0] * 51

gift_point = [0] * 51

def solution(friends, gifts):
    answer = 0

    for index in range(len(friends)):
        friends_map[friends[index]] = index

    for index in range(len(gifts)):
        giver, taker = gifts[index].split(" ")
        gift_map[friends_map[giver]][friends_map[taker]] += 1


    ## 선물지수 구하기
    for i in range(len(friends)):
        for j in range(len(friends)):
            gift_point[i] += gift_map[i][j]
            gift_point[i] -= gift_map[j][i]

    print(gift_point)

    for i in range(len(friends)):
        # index = friends_map[friends[i]]
        minus = 0
        plus = 0
        for j in range(len(friends)):

            ## i가 j에게 선물을 더 많이 줬다면
            if gift_map[i][j] > gift_map[j][i]:
                plus += 1

            if gift_map[i][j] == gift_map[j][i]:
                if gift_point[i] > gift_point[j]:
                    plus += 1

        point[i] = point[i] + plus - minus

    print(point)
    answer = max(point)
    return answer


# print(solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]))
print(solution(["joy", "brad", "alessandro", "conan", "david"], ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]))

