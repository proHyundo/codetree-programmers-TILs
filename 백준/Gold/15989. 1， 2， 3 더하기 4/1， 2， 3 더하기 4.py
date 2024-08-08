T = int(input())
lst = [int(input()) for _ in range(T)]
max_input = max(lst)
dp = [1] * (max_input+1)

for j in range(2, 4):
    for i in range(j, max_input+1):
        dp[i] = dp[i] + dp[i-j]


for ele in lst:
    print(dp[ele])