import itertools
import sys

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

houses = []
chicken = []

for i, row in enumerate(board):
    for j, ele in enumerate(row):
        if ele == 1:
            houses.append((i, j))
        elif ele == 2:
            chicken.append((i, j))

candidates = list(itertools.combinations(chicken, M))

answer = sys.maxsize
def get_min_distance(candidate):
    distance = 0
    for hx, hy in houses:
        min_val = sys.maxsize
        for cx, cy in candidate:
            min_val = min(min_val, abs(hx-cx) + abs(hy-cy))
        distance += min_val
    return distance

for candidate in candidates:
    answer = min(answer, get_min_distance(candidate))

print(answer)