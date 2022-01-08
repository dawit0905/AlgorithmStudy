x,y = map(str,input())
if x == 'a':
    x = 1
elif x == 'b':
    x=2
elif x == 'c':
    x=3
elif x == 'd':
    x=4
elif x == 'e':
    x=5
elif x == 'f':
    x=6
elif x == 'g':
    x=7
elif x == 'h':
    x=8
y = int(y)
dx = [2, 2,1,-1,-2,-2,-1,1]
dy = [1,-1,-2,-2,1,-1,2,2]

count = 0
for i in range(8):
    if 1 <= x+dx[i] <= 8 and 1 <= y+dy[i] <= 8 :
        count+=1

print(count)

'''
# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
'''



