# 문제 이름: 게임개발
# 해결 날짜: 240326
# 소요 시간: 49m
# 시간 복잡도: O(n^2)
# 난이도: 중
# 문제 URL: [해당되는 경우 문제의 URL 삽입]
# 해결 접근 방식: 
# - 방향과 관련 있어 dxs dys 기법을 사용
# - 방문 여부를 알아야 하기 때문에 _checked 2차원 리스트 사용
# 코멘트: [문제나 해결책과 관련된 추가 코멘트나 비고 사항.]

n, m = map(int, input().split())
x, y, cur_dir = map(int, input().split())

#      북 서  남 동
dxs = [0, 1, 0, -1]
dys = [-1, 0, 1, 0]
_board = [
    list(map(int, input().split())) for _ in range(n)
]
_checked = [
    [0] * m for _ in range(n)
]
_checked[x][y] = 1
ans = 1

while True:
    not_moved_cnt = 0
    for _ in range(0, 4):
        nx = x + dxs[cur_dir]
        ny = y + dys[cur_dir]

        if _board[nx][ny] == 0 and _checked[nx][ny] == 0:
            x = nx
            y = ny
            ans += 1
            _checked[x][y] = 1
            cur_dir = (cur_dir + 1) % 4
            break
        else:
            cur_dir = (cur_dir + 1) % 4
            not_moved_cnt += 1

    if not_moved_cnt == 4:
        x = x + dxs[(cur_dir + 1) % 4]
        y = y + dys[(cur_dir + 1) % 4]
        if _board[x][y] == 1:
            break

print(ans)
