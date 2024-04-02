# 문제 이름: 개미 전사
# 해결 날짜: 240401
# 소요 시간: 10분
# 시간 복잡도: O(n)
# 난이도: 하
# 문제 URL: [해당되는 경우 문제의 URL 삽입]
# 해결 접근 방식: [문제 해결에 접근한 방식을 간략히 설명. 여기에는 사용된 알고리즘, 데이터 구조 및 주목할 만한 최적화가 포함될 수 있음.]
# 코멘트: [문제나 해결책과 관련된 추가 코멘트나 비고 사항.]

N = int(input())
_list = list(map(int, input().split()))
_list[1] = max(_list[0], _list[1])

for i in range(2, len(_list)):
    _list[i] = max(_list[i-2] + _list[i], _list[i-1])

print(_list[N-1])