from collections import deque

N = int(input())
board = [
    list(input().split()) for _ in range(N)
]
teacher_lst = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 'T':
            teacher_lst.append((i, j))

answer = False


def check():
    q = deque()
    for ele in teacher_lst:
        q.append(ele)

    while q:
        ci, cj = q.popleft()
        # 우
        for j in range(cj+1, N):
            value = board[ci][j]
            if value == 'O':
                break
            elif value == 'S':
                return False
        # 좌
        for j in range(cj-1, -1, -1):
            value = board[ci][j]
            if value == 'O':
                break
            elif value == 'S':
                return False
        # 상
        for i in range(ci-1, -1, -1):
            value = board[i][cj]
            if value == 'O':
                break
            elif value == 'S':
                return False
        # 하
        for i in range(ci+1, N):
            value = board[i][cj]
            if value == 'O':
                break
            elif value == 'S':
                return False

    return True


def dfs(n, cnt):
    global answer
    if answer:
        return
    if cnt > 3:
        return
    if n == N ** 2:
        if cnt == 3:
            # for row in board:
            #     print(*row, sep='\t')
            # print('========')
            if check():
                answer = True
        return

    cx, cy = n // N, n % N
    if board[cx][cy] == 'X':
        board[cx][cy] = 'O'
        dfs(n + 1, cnt + 1)
        board[cx][cy] = 'X'
        dfs(n + 1, cnt)
    else:
        dfs(n + 1, cnt)


dfs(0, 0)
print('YES' if answer else 'NO')
