import sys


N = int(sys.stdin.readline())
arr = []
answer = [1,1,0,1,1]
heart = [0,0]

for _ in range(N):
    tmp = sys.stdin.readline().strip()
    arr.append(tmp)


body_x, body_y = 0, 0
flag = False
for i in range(N):
    for j in range(N):
        if arr[i][j] == '*':
            body_x, body_y = i, j
            heart[0], heart[1] = i+1+1,j+1
            flag = True
            break
    if flag:
        break

# 왼쪽 팔
# print(body_x, body_y)
t_x, t_y = body_x+1, body_y-1
while (0 <= t_y-1 < N) and arr[t_x][t_y-1] == '*':
    answer[0] += 1
    t_y -= 1

# 오른 팔
# print(body_x, body_y)
t_x, t_y = body_x+1, body_y+1
while (0 <= t_y+1 < N) and arr[t_x][t_y+1] == '*':
    answer[1] += 1
    t_y += 1

# 몸통
# print(body_x, body_y)
t_x, t_y = body_x+1, body_y
while arr[t_x+1][t_y] == '*':
    answer[2] += 1
    t_x += 1 

# 왼쪽 발
# print(body_x, body_y)
body_x, body_y = t_x, t_y
t_x, t_y = body_x+1, body_y-1
while (0 <= t_x+1 < N) and (0 <= t_y < N) and arr[t_x+1][t_y] == '*':
    answer[3] += 1
    t_x += 1

# 오른 발
# print(body_x, body_y)
t_x, t_y = body_x+1, body_y+1
while (0 <= t_x+1 < N) and (0 <= t_y < N) and arr[t_x+1][t_y] == '*':
    answer[4] += 1
    t_x += 1


print(*heart)
print(*answer)