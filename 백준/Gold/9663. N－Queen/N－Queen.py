N = int(input())
ans = 0

v_col = [False] * N
v_daegakup = [False] * (N * 2)
v_daegakdown = [False] * (N * 2)

def dfs(n, cnt):
    global ans
    if n == N:
        if cnt == N:
            ans += 1
        return

    for j in range(N):
        if not v_col[j] and not v_daegakdown[n-j] and not v_daegakup[n+j]:
            v_col[j] = True
            v_daegakdown[n-j] = True
            v_daegakup[n+j] = True
            dfs(n+1, cnt+1)
            v_col[j] = False
            v_daegakdown[n-j] = False
            v_daegakup[n+j] = False


dfs(0, 0)
print(ans)
