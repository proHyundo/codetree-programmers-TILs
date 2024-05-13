N = int(input())
up_check = [False] * (2*N)
right_cross_check = [False] * (2*N)
left_cross_check = [False] * (2*N)
ans = 0


def dfs(n):
    global ans
    if n == N:
        ans += 1
        return

    for j in range(N):
        if not up_check[j] and not right_cross_check[n + j] and not left_cross_check[n - j]:
            up_check[j] = True
            right_cross_check[n + j] = True
            left_cross_check[n - j] = True
            dfs(n + 1)
            up_check[j] = False
            right_cross_check[n + j] = False
            left_cross_check[n - j] = False


dfs(0)
print(ans)
