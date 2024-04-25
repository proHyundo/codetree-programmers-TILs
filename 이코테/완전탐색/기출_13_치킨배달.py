# 문제 이름: [문제 이름 삽입]
# 해결 날짜: [YY-MM-DD 형식으로 날짜 삽입]
# 소요 시간: [문제를 해결하는데 걸린 시간 삽입, 예: 45분]
# 시간 복잡도: [해결책의 시간 복잡도 삽입, 예: O(n), O(n^2) 등]
# 난이도: [난이도 수준 삽입, 예: 상, 중, 하]
# 문제 URL: [해당되는 경우 문제의 URL 삽입]
# 해결 접근 방식: [문제 해결에 접근한 방식을 간략히 설명. 여기에는 사용된 알고리즘, 데이터 구조 및 주목할 만한 최적화가 포함될 수 있음.]
# 코멘트: [문제나 해결책과 관련된 추가 코멘트나 비고 사항.]
import collections
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