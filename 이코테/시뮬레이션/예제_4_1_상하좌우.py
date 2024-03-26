# 문제 이름: 상하좌우
# 해결 날짜: 240326
# 소요 시간: 8 min
# 시간 복잡도: O(n)
# 난이도: 하
# 문제 URL: [해당되는 경우 문제의 URL 삽입]
# 해결 접근 방식: 이동 방법이 "L, R, U, D"으로 한정 되어 있기 때문에 key-value 형태인 dictionary 사용
# 코멘트: [문제나 해결책과 관련된 추가 코멘트나 비고 사항.]

direction = {
    "L": [0,-1],
    "R": [0,1],
    "U": [-1,0],
    "D": [1,0]
}

n = int(input())
plan = list(input().split())

x = 1
y = 1


def is_in_board(nx, ny):
    global n
    if 1 <= nx <= n and 1 <= ny <= n:
        return True
    else:
        return False


for p in plan:
    dx, dy = direction.get(p)
    nx = x + dx
    ny = y + dy
    if is_in_board(nx, ny):
        x = nx
        y = ny
    else:
        continue

print(x, y)