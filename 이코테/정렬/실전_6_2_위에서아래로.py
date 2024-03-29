# 문제 이름: 위에서아래로
# 해결 날짜: 240328
# 소요 시간: 2m
# 시간 복잡도: O(n log n)
# 난이도: 하
# 문제 URL: [해당되는 경우 문제의 URL 삽입]
# 해결 접근 방식: [문제 해결에 접근한 방식을 간략히 설명. 여기에는 사용된 알고리즘, 데이터 구조 및 주목할 만한 최적화가 포함될 수 있음.]
# 코멘트: [문제나 해결책과 관련된 추가 코멘트나 비고 사항.]

N = int(input())
_list = [
    int(input()) for _ in range(N)
]
print(sorted(_list, reverse=True))
