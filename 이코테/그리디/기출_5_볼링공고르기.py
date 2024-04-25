# 문제 이름: 볼링공 고르기
# 해결 날짜: 240415
# 소요 시간: 5분
# 시간 복잡도: O(n^2)
# 난이도: 하
# 문제 URL: [해당되는 경우 문제의 URL 삽입]
# 해결 접근 방식: 시간복잡도를 더 줄일 수 있는 방법이 있을 거 같은데...
# 코멘트: [문제나 해결책과 관련된 추가 코멘트나 비고 사항.]

N, M = map(int, input().split())
_list = list(map(int, input().split()))
cnt = 0
for i in range(0, N-1):
    for j in range(i+1, N):
        if _list[i] == _list[j]:
            continue
        print(i+1, '번, ', j+1, '번')
        cnt += 1

print(cnt)