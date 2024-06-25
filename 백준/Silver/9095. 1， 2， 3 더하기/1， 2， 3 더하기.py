N = int(input())
lst = []
max_index = 0

for _ in range(N):
    tmp = int(input())
    lst.append(tmp)
    if max_index < tmp:
        max_index = tmp

dp = [1, 1, 2, 4] + [0] * (max_index - 3)

if max_index > 3:
    for i in range(4, max_index+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for index in lst:
    print(dp[index])
