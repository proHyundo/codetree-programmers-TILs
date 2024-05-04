T = int(input())
for test_case in range(1, T+1):
    
    cost = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    
    ans = 3000 * 30 * 12
    
    def dfs(n, total):
        global ans
        if ans <= total:
            return
    
        if n >= 12:
            ans = min(ans, total)
            return
    
        # 하부 함수 호출
        if plan[n] != 0:
            # 1일 이용권
            dfs(n+1, total + (plan[n] * cost[0]))
            # 한 달 이용권
            dfs(n+1, total + cost[1])
            # 세 달 이용권
            dfs(n+3, total + cost[2])
            # 일 년 이용권
            dfs(n+12, total + cost[3])
        else:
            dfs(n+1, total)
    
    dfs(0, 0)
    print(f'#{test_case}', ans)
