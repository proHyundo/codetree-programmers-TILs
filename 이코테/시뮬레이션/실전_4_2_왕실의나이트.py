# 문제 이름: 왕실의나이트
# 해결 날짜: 240326
# 소요 시간: 8m 30s
# 시간 복잡도: O(n)
# 난이도: 하
# 문제 URL: [해당되는 경우 문제의 URL 삽입]
# 해결 접근 방식: 나이트가 이동할 수 있는 경우의 수는 dxs dys 기법을 사용. 알파벳으로 주어지는 y좌표는 dictionary 를 이용해 숫자로 치환
# 코멘트: [문제나 해결책과 관련된 추가 코멘트나 비고 사항.]

dxs = [-2, -1, 1, 2, 2, 1, -1, -2]
dys = [1, 2, 2, 1, -1, -2, -2, -1]
alpha_to_num = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}  # ord() 함수로 개선할 수 있음
ans = 0

current = input()
x = int(current[1])
y = alpha_to_num.get(current[0])


def is_in_board(nx, ny):
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        return True
    else:
        return False


for dx, dy in zip(dxs, dys):
    nx = x + dx
    ny = y + dy
    if is_in_board(nx, ny):
        ans += 1

print(ans)
