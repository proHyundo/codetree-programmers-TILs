N, K = map(int, input().split())
memo = [0] * 100001

def dfs(locate, time):
    if locate == K:
        return

    if locate - 1 > 0:
        memo[locate - 1] = time
        dfs(locate - 1, time + 1)
    if locate + 1 < 100001:
        memo[locate + 1] = time
        dfs(locate + 1, time + 1)
    if locate * 2 < 100001:
        memo[locate * 2] = time
        dfs(locate * 2, time)

dfs(N, 0)
print(memo[K])