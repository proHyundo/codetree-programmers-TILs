T = int(input())
for test_case in range(1, T + 1):
    number, s_cnt = input().split()
    nums = list(number)  # 숫자 리스트
    N = int(s_cnt)  # 교환 횟수
    length = len(nums)
    ans = 0
    visited = dict()  # 해당 문제의 경우 visited를 dictionary 구조로 활용해도 됨.


    def dfs(n):
        global ans

        if n == N:
            ans = max(ans, int(''.join(nums)))
            return

        for i in range(length-1):
            for j in range(i+1, length):
                nums[i], nums[j] = nums[j], nums[i]

                chk = int(''.join(nums)) * 10 + n  # (int(''.join(nums)), n) 과 같은 tuple 형식보다, 해당 방법이 유니크함을 보장하면서 조금 더 빠름
                if chk not in visited:
                    dfs(n+1)
                    visited[chk] = True

                nums[i], nums[j] = nums[j], nums[i]


    dfs(0)
    print(f'#{test_case}', ans)