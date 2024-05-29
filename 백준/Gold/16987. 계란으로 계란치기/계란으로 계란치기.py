N = int(input())
arr = [
    list(map(int, input().split())) for _ in range(N)
    ]
ans = 0


def dfs(n, c):
    global ans
    if c == N:
        ans = N
        return

    if n == N:
        ans = max(ans, c)
        return

    if arr[n][0] <= 0:
        dfs(n+1, c)
    else:
        all_broke = True
        for i in range(N):
            if i != n and arr[i][0] > 0:  # 타겟한 계란이 깨진 계란이 아니라면
                all_broke = False
                arr[i][0] -= arr[n][1]
                arr[n][0] -= arr[i][1]
                dfs(n+1, c + int(arr[i][0]<=0) + int(arr[n][0]<=0))
                arr[i][0] += arr[n][1]
                arr[n][0] += arr[i][1]
        if all_broke:
            dfs(n+1, c)

dfs(0, 0)
print(ans)