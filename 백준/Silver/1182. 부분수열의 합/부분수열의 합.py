N, S = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0


def dfs(n, cnt, total):
    global ans
    if n == N:
        if total == S and cnt > 0:
            ans += 1
        return

    dfs(n + 1, cnt + 1, total + arr[n])
    dfs(n + 1, cnt, total)

dfs(0, 0, 0)
print(ans)