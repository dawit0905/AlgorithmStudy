import sys


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

score = [0] * (n+1)
target_list = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    tmp = list(map(int, sys.stdin.readline().split()))

    # 타켓 맞췄으면 +1
    for j in range(0, len(tmp)):
        if tmp[j] == target_list[i]:
            score[j+1] += 1

    # 예상이 빗나간 수 체크 후, 타켓 추가점수 주기
    score[target_list[i]] += len(tmp) - tmp.count(target_list[i])

for i in score[1:]:
    print(i)
