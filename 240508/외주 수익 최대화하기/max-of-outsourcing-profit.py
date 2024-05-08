import sys

N = int(input())
t_list = []
p_list = []

for _ in range(N):
    a, b = map(int, input().split())
    t_list.append(a)
    p_list.append(b)

ans = -sys.maxsize


def dfs(n, profit, sm):
    global ans
    if n == N:
        ans = max(ans, profit)
        return
    
    # 남은 작업량이 없다면
    if sm == 0:
        # 외주를 받는다면 : 다음 날짜로, 수익을 챙기고, 작업량이 생기고
        dfs(n+1, profit + p_list[n], t_list[n] - 1)
        # 외주를 받지 않는다면 : 다음 날짜로, 수익은 그대로, 작업량 0
        dfs(n+1, profit, 0)
    else:
        # 현재 작업중이라, 다음 날짜로, 수익은 그대로, 작업량 - 1
        dfs(n+1, profit, sm-1)


dfs(0, 0, 0)
print(ans)