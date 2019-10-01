import sys
# 백준 14646 문제
# N 동안의 저녁메뉴를 미리 고르기로 했다.
# 돌림판을 돌리고 돌림판에 걸린 칸을 확인한다.
# 0 걸린 칸에 스티커가 붙어있지 않다면, 스티커를 하나 붙인다.
# 1 걸린 칸에 스티커가 붙어있다면, 식단표에 해당하는 메뉴를 적어넣고 그 칸을 제거한다.
# 2 (스티커도 떼어낸다) 욱제의 돌림판은 특별해서 어떤 칸이 제거되면 다음부터는 그 칸에 절대로 멈추지 않는 마법이 걸려있다. (!)
# 모든 칸이 제거될 때 까지 (0, 1, 2)을 반복한다.


n = int(sys.stdin.readline())
list = list(map(int, sys.stdin.readline().split()))
check_list = [0 for i in range(len(list))]
max_num = 0
now_num = 0

# 5
# 1 2 1 3 4 5 2 3 4 5

for i in list:
    check_list[i] += 1

    if check_list[i] != 2:
        now_num += 1
    else :
        now_num -= 1

    if max_num < now_num:
        max_num = now_num


    print(i,"일때 max: ",max_num," + now: ",now_num)


print(max_num)