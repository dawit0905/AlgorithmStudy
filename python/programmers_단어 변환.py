from collections import deque


def solution(begin, target, words):
    # 1. 시작 조건 확인: target이 words에 없으면 변환 불가
    if target not in words:
        return 0

    q = deque([(begin, 0)])
    visited = {begin}

    while q:
        current_word, count = q.popleft()

        if current_word == target:
            return count

        for next_word in words:
            if next_word not in visited:
                diff = 0
                for c1, c2 in zip(current_word, next_word):
                    if c1 != c2:
                        diff += 1

                if diff == 1:
                    visited.add(next_word)
                    q.append((next_word, count + 1))

    return 0


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
