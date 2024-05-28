N = int(input())
arr = [0] + list(map(int, input().split()))
dp = [1] * (N+1)


for i in range(2, N+1):
    mv = 0
    for j in range(1, i):
        if arr[i] > arr[j]:
            mv = max(mv, dp[j])
    dp[i] = mv + 1

print(max(dp))