# 이진 트리로 완전탐색 해야 할 것 같음.
# 가지치기 가능할듯
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    foods = [
        list(map(int, input().split())) for _ in range(N)
    ]

    ans = 20000 * N * N


    def dfs(n, alst, blst):
        global ans
        if n == N:
            if len(alst) >= 2 and len(blst) >= 2:
                asum = bsum = 0
                for i in alst:
                    for j in alst:
                        asum += foods[i][j]
                for i in blst:
                    for j in blst:
                        bsum += foods[i][j]
                ans = min(ans, abs(asum-bsum))
            return

        dfs(n+1, alst + [n], blst)
        dfs(n+1, alst, blst+[n])


    dfs(0, [], [])
    print(f'#{test_case}', ans)
