def solution(citations):
    # 1. 인용 횟수를 내림차순으로 정렬
    citations.sort(reverse=True)

    # 2. 정렬된 리스트를 순회하며 h-index 찾기
    for i, citation_count in enumerate(citations):
        # "h편 이상" 에서 h는 인덱스+1 과 같다
        h = i + 1
        # 인용 횟수가 논문 편수(h)보다 작아지는 순간이 h-index
        if citation_count < h:
            return i  # 이전의 h가 최댓값이므로 i가 정답

    # 모든 논문이 n편 이상 인용되었다면, 논문 개수가 h-index
    return len(citations)

print(solution([3, 0, 6, 1, 5]))
