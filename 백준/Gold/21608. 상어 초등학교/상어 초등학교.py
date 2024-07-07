from collections import deque

N = int(input())
# 배치를 완료한 리스트
board = [
    [0] * N for _ in range(N)
]
dictionary = dict()


def get_like_xy(me, nums):
    max_lst = []
    max_cnt = 0
    for ci in range(N):
        for cj in range(N):
            # board 에 비어 있으면, 4 방향 순회해서, 범위 안, nums에 포함된 숫자면, cnt + 1
            if board[ci][cj] == 0:
                cnt = 0
                for di, dj in zip([0, 1, 0, -1], [1, 0, -1, 0]):
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < N and 0 <= nj < N and board[ni][nj] in nums:
                        cnt += 1
                if cnt == max_cnt:
                    max_lst.append((ci, cj))
                elif cnt > max_cnt:
                    max_cnt = cnt
                    max_lst = [(ci, cj)]

    return max_lst

def get_max_empty_xy(llst):
    empty_lst = []
    max_cnt = 0
    for ci, cj in llst:
        cnt = 0
        for di, dj in zip([0, 1, 0, -1], [1, 0, -1, 0]):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 0:
                cnt += 1
        if cnt == max_cnt:
            empty_lst.append((ci, cj))
        elif cnt > max_cnt:
            max_cnt = cnt
            empty_lst = [(ci, cj)]
    return empty_lst


for _ in range(N ** 2):
    lst = list(map(int, input().split()))
    dictionary[lst[0]] = lst[1:]

    # 좋아하는 학생이 인접한 칸에 가장 많은 칸 반환
    like_lst = get_like_xy(lst[0], lst[1:])

    # 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
    if len(like_lst) == 1:
        board[like_lst[0][0]][like_lst[0][1]] = lst[0]
    else:
        # 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
        emptiest_lst = get_max_empty_xy(like_lst)
        if len(emptiest_lst) == 1:
            board[emptiest_lst[0][0]][emptiest_lst[0][1]] = lst[0]
        else:
            # 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
            emptiest_lst.sort(key = lambda x: (x[0], x[1]))
            board[emptiest_lst[0][0]][emptiest_lst[0][1]] = lst[0]

# for row in board:
#     print(*row, sep='\t')

answer = 0

for ci in range(N):
    for cj in range(N):
        cnt = 0
        for di, dj in zip([0, 1, 0, -1], [1, 0, -1, 0]):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and board[ni][nj] in dictionary[board[ci][cj]]:
                cnt += 1
        answer += 10 ** (cnt-1) if cnt > 0 else 0

print(answer)