N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
checked = [False] * N
ans = set()


def dfs(n, lst):
    if n == M:
        ans.add(tuple(lst))
        return
    for i in range(len(nums)):
        if not checked[i]:
            checked[i] = True
            dfs(n+1, lst + [nums[i]])
            checked[i] = False


dfs(0, [])
_ans = sorted(list(ans))
for ele in _ans:
    print(*ele)

