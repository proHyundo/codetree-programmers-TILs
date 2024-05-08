T = int(input())
for test_case in range(1, T+1):
    inputs = list(map(int, input().split()))
    N = inputs[0]  # 5
    stations = [0] + inputs[1:]  # 2 3 1 1
    ans = 100 * 100


    def dfs(n, cnt, charged):
        global ans
        if ans < cnt:
            return

        if n == N:
            ans = min(ans, cnt)
            return

        # 교체 O
        dfs(n+1, cnt+1, stations[n]-1)
        if charged > 0:
            dfs(n+1, cnt, charged-1)


    dfs(2, 0, stations[1]-1)
    print(f'#{test_case}', ans)
