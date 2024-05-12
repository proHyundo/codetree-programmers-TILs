N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
checked = [False] * N
ans = set()


def dfs(n, lst, start):
    global ans
    if n == M:
        ans.add(tuple(lst))
        return

    for i in range(start, N):
        if not checked[i]:
            checked[i] = True
            dfs(n+1, lst + [nums[i]], i)
            checked[i] = False


dfs(0, [], 0)
for ele in sorted(list(ans)):
    print(*ele)
