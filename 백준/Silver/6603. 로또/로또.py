while True:
    inputs = list(map(int, input().split()))
    K = inputs[0]
    if K == 0:
        break

    nums = sorted(inputs[1:])
    ans = set()

    def dfs(n, lst, cnt):
        if cnt > 6:
            return

        if n == K:
            if cnt == 6:
                ans.add(tuple(lst))
            return

        dfs(n+1, lst + [nums[n]], cnt+1)
        dfs(n+1, lst, cnt)


    dfs(0, [], 0)
    for ele in sorted(list(ans)):
        print(*ele)

    print()
