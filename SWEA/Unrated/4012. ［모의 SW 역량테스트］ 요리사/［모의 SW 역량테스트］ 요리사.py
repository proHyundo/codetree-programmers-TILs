T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    foods = [
        list(map(int, input().split())) for _ in range(N)
    ]

    ans = 20000 * N * N
    alst = []
    blst = []

    def dfs(n):
        global ans
        if n == N:
            if len(alst) >= 2 and len(blst) >= 2:  # 식재료 개수 N을 2로 나눈다고 했기 때문에 `len(alst) == N // 2` 으로 변경하는 것이 좋아보임.
                asum = bsum = 0
                for i in alst:
                    for j in alst:
                        asum += foods[i][j]
                for i in blst:
                    for j in blst:
                        bsum += foods[i][j]
                ans = min(ans, abs(asum-bsum))
            return
        alst.append(n)
        dfs(n+1)
        alst.pop()

        blst.append(n)
        dfs(n+1)
        blst.pop()


    dfs(0)
    print(f'#{test_case}', ans)
