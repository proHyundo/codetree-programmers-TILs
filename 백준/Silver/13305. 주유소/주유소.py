import sys

input = sys.stdin.readline
N = int(input())
load_lst = [0] + list(map(int, input().split()))     # 2 3 1
cost_lst = [0] + list(map(int, input().split()))    # 5 2 4 1

min_cost = cost_lst[1]
sm_cost = 0

for i in range(1, N):
    if min_cost > cost_lst[i]:
        min_cost = cost_lst[i]
    sm_cost += min_cost * load_lst[i]

print(sm_cost)