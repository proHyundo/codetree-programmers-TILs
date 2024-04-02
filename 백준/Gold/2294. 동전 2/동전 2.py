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