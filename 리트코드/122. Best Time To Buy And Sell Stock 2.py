def sol(prices):
    L = len(prices)
    dp = [
        [0] * L for _ in range(L)
    ]
    for i in range(L):
        dp[i][0] = 0

    for i in range(L):
        for j in range(1, L):

                # dp[i][j] = max(dp[i][j - 1], prices[j] - prices[i])

            if i < j and prices[i] < prices[j]:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][i] + prices[j] - prices[i])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    for row in dp:
        print(*row, sep='\t')

    return dp[L-1][L-1]

#   7 1 5 3 6 4
# 7 0 0 0 0 0 0
# 1 0 0 4 4 5 5
# 5 0 0 4 4 5 5
# 3 0 0 4 4 7 7
# 6 0 0 4 4 7 7
# 4 0 0 4 4 7 7

# print(sol([1,2,3,4,5]))

def sol2(prices):
    ans = 0
    L = len(prices)
    for i in range(L-1):
        if prices[i] < prices[i+1]:
            ans += prices[i+1] - prices[i]

    return ans

print(sol2([7,1,5,3,6,4]))
