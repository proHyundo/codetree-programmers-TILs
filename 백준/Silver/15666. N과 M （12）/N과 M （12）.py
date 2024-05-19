N, M = map(int,input().split())
arr = sorted(list(map(int,input().split())))
ans = set()


def dfs(n, lst, start):
    if n == M:
        ans.add(tuple(lst))
        return

    for i in range(start, N):
        dfs(n+1, lst + [arr[i]], i)


dfs(0, [], 0)
for ele in sorted(list(ans)):
    print(*ele)