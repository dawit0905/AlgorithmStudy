N = int(input())
moving_array = list(input().rstrip().split())
x,y = 1,1
# 동 북 서 남
dx = [1,0,-1,0]
dy = [0,-1,0,1]

for vector in moving_array:
    if vector == 'R' and x != N:
        x+=dx[0]
        y+=dy[0]
    elif vector =='U' and y != 1:
        x += dx[1]
        y += dy[1]
    elif vector =='L' and x != 1:
        x += dx[2]
        y += dy[2]
    elif vector =='D' and y != N:
        x += dx[3]
        y += dy[3]

print(x, y)