T = int(input())
for test_case in range(1, T+1):
    
    N = int(input())
    operations = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    max_ans = -100000000
    min_ans = 100000000


    def dfs(n, result):
        global max_ans, min_ans
        if n == N:
            max_ans = max(max_ans, result)
            min_ans = min(min_ans, result)
            return

        for i in range(4):
            if operations[i] != 0:
                if i == 0:
                    operations[i] -= 1
                    dfs(n + 1, result + nums[n])
                    operations[i] += 1
                elif i == 1:
                    operations[i] -= 1
                    dfs(n + 1, result - nums[n])
                    operations[i] += 1
                elif i == 2:
                    operations[i] -= 1
                    dfs(n + 1, result * nums[n])
                    operations[i] += 1
                elif i == 3:
                    operations[i] -= 1
                    dfs(n + 1, int(result / nums[n]))
                    operations[i] += 1


    dfs(1, nums[0])
    print(f'#{test_case}', max_ans - min_ans)