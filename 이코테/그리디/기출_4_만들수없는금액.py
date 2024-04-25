# 문제 이름: [문제 이름 삽입]
# 해결 날짜: [YY-MM-DD 형식으로 날짜 삽입]
# 소요 시간: [문제를 해결하는데 걸린 시간 삽입, 예: 45분]
# 시간 복잡도: [해결책의 시간 복잡도 삽입, 예: O(n), O(n^2) 등]
# 난이도: [난이도 수준 삽입, 예: 상, 중, 하]
# 문제 URL: [해당되는 경우 문제의 URL 삽입]
# 해결 접근 방식: 시간내 풀지 못함
# 코멘트: [문제나 해결책과 관련된 추가 코멘트나 비고 사항.]

N = int(input())
_list = list(map(int, input().split()))
_list.sort()

target = 1
for x in _list:
    if target < x:
        break
    target += x

print(target)

