# 문제 이름: 성적이 낮은 순서로 학생 출력하기
# 해결 날짜: 240328
# 소요 시간: 6m
# 시간 복잡도: O(n log n)
# 난이도: 하
# 문제 URL: [해당되는 경우 문제의 URL 삽입]
# 해결 접근 방식: [문제 해결에 접근한 방식을 간략히 설명. 여기에는 사용된 알고리즘, 데이터 구조 및 주목할 만한 최적화가 포함될 수 있음.]
# 코멘트: 데이터를 입력 받을 때 score를 int 로 받을 수 있는 방법은 다음과 같음.
# name_with_score = [
#     (name, int(grade)) for name, grade in (input().split() for _ in range(N))
# ]

N = int(input())
name_with_score = [
    tuple(input().split()) for _ in range(N)
]

name_with_score.sort(key = lambda x : int(x[1]))

for a in name_with_score:
    print(a[0], end = ' ')