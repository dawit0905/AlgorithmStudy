import sys

'''
def recur(x, y, )
size : 현재 배열의 크기
x : 배열의 가장 위쪽
y : 배열의 가장 왼쪽
pos : -1 or 분할하면서 L트로미노가 들어간 구역의 포지션
4분할로 표시할듯? x, y을 입력받고 어디 구역인지 알려주는 function이 필요할려나?
12
34

'''
def recur(size, x, y, target):
    global cnt
    # k가 2가되면 그냥 0(업데이트 안된 것)인 부분들을 그냥 채우면된다.
    if size == 2:
        for i in range(x, x+2):
            for j in range(y, y+2):
                if arr[i][j] == 0:
                    arr[i][j] = cnt
        cnt += 1

    # 1. 여기서는 divide 하기 전에! -1(하수구)가 포함되어 있는 칸 대각선 방향 정 가운데에
    # L트로미노를 채워야된다.
    # 2. 그다음 4분할로 나눈다. (아마 구현할 때, 머가 더 튀어나올듯?;;)
    else:
        # 1번 실행

        mid = size // 2
        mid_minus_one = mid - 1

        # target = check(x, y, size)
        for i in range(0, 2):
            for j in range(0, 2):
                if pos_except[target][0] == i and pos_except[target][1] == j:
                    continue
                arr[i+mid_minus_one][j+mid_minus_one] = cnt

        cnt += 1

        # 1사분면
        recur(size//2, 0, 0, target)
        # 2사분면
        recur(size // 2, 0, mid, target)
        # 3사분면
        recur(size // 2, mid, 0, target)
        # 4사분면
        recur(size // 2, mid, mid, target)

# 어떤 -1이 사분면에 해당하는지 체크
def check(x, y, size):
    mid = size // 2
    if 0 <= x < mid and 0 <= y < mid:
        return 1
    elif 0 <= x < mid and mid <= y < size:
        return 2
    elif mid <= x < size and 0 <= y < mid:
        return 3
    elif mid <= x < size and mid <= y < size:
        return 4


k = int(sys.stdin.readline())
y, x = map(int, sys.stdin.readline().split())
arr = [[0] * (2**k) for _ in range((2**k))]
cnt = 1
pos_except = {1: (0, 0), 2: (0, 1), 3: (1, 0), 4: (1, 1)}

x = (2**k) - x
y = y - 1

recur(2**k, 0, 0, check(x, y, 2**k))
arr[x][y] = -1
for i in arr:
    print(*i)
