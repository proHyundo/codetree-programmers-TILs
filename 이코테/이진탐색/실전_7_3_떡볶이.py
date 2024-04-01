# 문제 이름: 떡볶이 떡 만들기
# 해결 날짜: 240329
# 소요 시간: 13m
# 시간 복잡도: O(n^2)
# 난이도: 중
# 문제 URL: [해당되는 경우 문제의 URL 삽입]
# 해결 접근 방식: 순차탐색으로 풀이했으나, 시간초과가 발생할 것이다.
# 코멘트: pivot을 이진탐색으로 탐색했어야 한다.

N, M = map(int, input().split())
_list = list(map(int, input().split()))

start = 0
end = max(_list) - 1
ans = 0

while start <= end:
    sum = 0
    mid = (start + end) // 2

    for i in _list:
        sum += (i - mid) if (i - mid) > 0 else 0

    if sum >= M:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)



