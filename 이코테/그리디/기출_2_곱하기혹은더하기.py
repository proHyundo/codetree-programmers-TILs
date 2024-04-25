# 문제 이름: 곱하기 혹은 더하기
# 해결 날짜: 240408
# 소요 시간: 6분
# 시간 복잡도: O(n)
# 난이도: 하
# 문제 URL: [해당되는 경우 문제의 URL 삽입]
# 해결 접근 방식: [문제 해결에 접근한 방식을 간략히 설명. 여기에는 사용된 알고리즘, 데이터 구조 및 주목할 만한 최적화가 포함될 수 있음.]
# 코멘트: prod가 1인 경우에도 더하기 연산을 수행하는 것이 최댓값을 도출할 수 있다.

_list = list(map(int, input()))
prod = _list[0]

for i in range(1, len(_list)):
    if prod <= 1 or _list[i] <= 1:
        prod = prod + _list[i]
    else:
        prod = prod * _list[i]

print(prod)
