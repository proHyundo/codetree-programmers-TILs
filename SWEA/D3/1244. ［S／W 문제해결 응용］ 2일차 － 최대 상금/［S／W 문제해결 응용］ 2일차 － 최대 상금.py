T = int(input())
for test_case in range(1, T + 1):
    number, s_cnt = input().split()
    nums = list(number)  # 숫자 리스트
    N = int(s_cnt)  # 교환 횟수
    length = len(nums)
    ans = 0
    visited = dict()


    def dfs(n):
        global ans

        if n == N:
            ans = max(ans, int(''.join(nums)))
            return

        for i in range(length-1):
            for j in range(i+1, length):
                nums[i], nums[j] = nums[j], nums[i]

                chk = int(''.join(nums)) * 10 + n
                if chk not in visited:
                    dfs(n+1)
                    visited[chk] = True

                nums[i], nums[j] = nums[j], nums[i]


    dfs(0)
    print(f'#{test_case}', ans)