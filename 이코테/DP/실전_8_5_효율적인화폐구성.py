# 문제 이름: 효율적인 화폐 구성
# 해결 날짜: 240401
# 소요 시간: 26분
# 시간 복잡도: O(n^2)
# 난이도: 하
# 문제 URL: https://www.acmicpc.net/problem/2294
# 해결 접근 방식:
# - 화폐의 가치가 항상 배수 관계가 아니라 그리디로는 해결이 안됨. 그래서 DP로 풀이하기로 결정.
# - DP 의 길이는 최종 목표인 합 k원 이라서 0번째 인덱스 제외하고 (K+1) 길이로 지정.
# - 동일한 가치의 동전이 주어질 수 있으니 set 자료구조 선택. 화폐 주어질 때 DP 테이블에 1 초기화
# - 화폐 가치 1 부터 화폐 가치 K 까지 순회하면서, 만약 순회 대상이 초기화 되지 않았을 경우, set 화폐 종류를 순회해 가장 적은 개수로 초기화.
# 코멘트: [문제나 해결책과 관련된 추가 코멘트나 비고 사항.]
import sys

n, k = map(int, input().split())
dp = [sys.maxsize] * (k+1)
_set = set()

for _ in range(n):
    num = int(input())
    _set.add(num)
    if num < k+1:
        dp[num] = 1


for i in range(1, k+1):
    if dp[i] == sys.maxsize:
        for s in _set:
            if i-s > 0:
                dp[i] = min(dp[i], dp[i-s]+1)

print(-1 if dp[k] == sys.maxsize else dp[k])