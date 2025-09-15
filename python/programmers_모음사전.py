def solution(word: str) -> int:
    answer = 0
    words = ['A', 'E', 'I', 'O', 'U']

    def check(text: str):
        nonlocal answer
        answer += 1
        if text == word:
            return 1
        else:
            return 0

    for a in words:
        if check(a):
            return answer
        for e in words:
            if check(a + e):
                return answer
            for i in words:
                if check(a + e + i):
                    return answer
                for o in words:
                    if check(a + e + i + o):
                        return answer
                    for u in words:
                        if check(a + e + i + o + u):
                            return answer


print(solution("AAAAE"))
