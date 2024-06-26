# 문제 이름: 바닥공사
# 해결 날짜: 240401
# 소요 시간: 8분
# 시간 복잡도: O(n)
# 난이도: 하
# 문제 URL:
# 해결 접근 방식: 전형적인 DP 문항
# 코멘트: 2가지 경우의 수로 갈라지기 때문에, 더하는 것이 아니라 곱해야 한다.

N = int(input())
dp = [0] * (N + 1)

dp[1] = 1
dp[2] = 2
for i in range(3, N+1):
    dp[i] = (dp[i-1]) + (dp[i-2] * 2)

print(dp)
print(dp[N] % 796796)
