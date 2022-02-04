n, m = map(int, input().split())
idx = list(map(int, input().split()))

step = 0


def move_left(que):
    global step
    step += 1

    tmp = que.pop(0)
    que.append(tmp)


def move_right(que):
    global step
    step += 1

    tmp = [que.pop(-1)]
    tmp.extend(que)
    que = tmp

    return que


que = list(range(1, n + 1))

while idx:
    if que[0] == idx[0]:
        que.pop(0)
        idx.pop(0)
    else:
        if que.index(idx[0]) <= len(que) // 2:
            while que[0] != idx[0]: move_left(que)
        else:
            while que[0] != idx[0]: que = move_right(que)

print(step)
