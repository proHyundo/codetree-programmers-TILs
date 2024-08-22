import sys

input = sys.stdin.readline
N = int(input())

load_lst = [0] + list(map(int, input().split()))     # 2 3 1
cost_lst = [0] + list(map(int, input().split()))    # 5 2 4 1

if cost_lst.count(1) == N:
    print(sum(load_lst))
else:
    DP = [0] + [sys.maxsize] * N
    DP[2] = cost_lst[1] * load_lst[1]

    for i in range(1, N): # i = 1,2,3번 도시에서 주유
        for j in range(i+1, N+1): # j = 2,3,4번 도시로 이동
            DP[j] = min(DP[j], DP[j-1] + (cost_lst[i] * load_lst[j-1]))
        # print(DP)

    print(DP[N])
