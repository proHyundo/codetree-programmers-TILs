# 문제 이름: 문자열뒤집기
# 해결 날짜: 240408
# 소요 시간: 10분
# 시간 복잡도: O(n)
# 난이도: 하
# 문제 URL: [해당되는 경우 문제의 URL 삽입]
# 해결 접근 방식: [문제 해결에 접근한 방식을 간략히 설명. 여기에는 사용된 알고리즘, 데이터 구조 및 주목할 만한 최적화가 포함될 수 있음.]
# 코멘트: 나의 풀이는 이전 인덱스와 현재 인덱스를 비교하는 반면, 이코테 풀이는 현재 인덱스와 다음 인덱스를 비교한다. 차이 없음.

# 0 그룹 개수, 1 그룹 개수

_list = list(map(int, input()))
zero_cnt = 0
one_cnt = 0

if _list[0] == 0:
    zero_cnt += 1
else:
    one_cnt += 1

for i in range(1, len(_list)):
    if _list[i-1] != _list[i]:
        if _list[i] == 0:
            zero_cnt += 1
        else:
            one_cnt += 1

print(min(zero_cnt, one_cnt))