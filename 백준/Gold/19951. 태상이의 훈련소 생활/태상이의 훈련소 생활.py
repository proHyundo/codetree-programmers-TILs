import sys

input = sys.stdin.readline
N, M = map(int, input().split())    # 칸, 조교
h_lst = [0] + list(map(int, input().split())) # 칸마다 높이
t_lst = [0] * (N+2)
for _ in range(M):
    a, b, k = map(int, input().split()) # a ~ b k 만큼
    if k >= 0:
        t_lst[a] += abs(k)
        t_lst[b+1] -= abs(k)
    else:
        t_lst[a] -= abs(k)
        t_lst[b+1] += abs(k)

for i in range(1, N+1):
    t_lst[i] += t_lst[i-1]

for i in range(1, N+1):
    print(h_lst[i] + t_lst[i], end=' ')