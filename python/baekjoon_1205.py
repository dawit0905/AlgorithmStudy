import sys

def solve():
    input = sys.stdin.readline
    N, new_point, P = map(int, input().split())

    if N == 0:
        print(1)
        return

    arr = list(map(int, input().split()))
    # 입력이 이미 비오름차순이므로 정렬 불필요
    # 리스트가 꽉 찼고 새 점수가 마지막 점수 이하라면 불가
    if N == P and new_point <= arr[-1]:
        print(-1)
        return

    rank = 1
    for score in arr:
        if score > new_point:
            rank += 1
        else:
            break
    print(rank)

if __name__ == "__main__":
    solve()
