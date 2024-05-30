N = int(input())

columns = [False] * N
lower_dia = [False] * (2*N + 1)
upper_dia = [False] * (2*N + 1)

ans = 0


def dfs(n):
    global ans
    if n == N:
        ans += 1
        return

    for i in range(N):
        if not columns[i] and not lower_dia[n-i] and not upper_dia[n+i]:
            columns[i] = True
            lower_dia[n-i] = True
            upper_dia[n+i] = True
            dfs(n+1)
            columns[i] = False
            lower_dia[n - i] = False
            upper_dia[n + i] = False

dfs(0)
print(ans)