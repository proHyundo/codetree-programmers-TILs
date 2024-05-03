# 재귀를 사용해 제출했던 풀이와 달리, while 문을 사용해 풀이했다.
# 참고 링크 : https://youtu.be/rw2gQg9x_EA
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    ans = [
        [0] * N for _ in range(N)
    ]

    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]

    i, j, cnt, dir = 0, 0, 1, 0
    ans[i][j] = cnt
    cnt += 1

    while cnt <= N ** 2:
        ni, nj = i + dxs[dir], j + dys[dir]
        if 0 <= ni < N and 0 <= nj < N and ans[ni][nj] == 0:
            i, j = ni, nj
            ans[i][j] = cnt
            cnt += 1
        else:
            dir = (dir + 1) % 4



    print(f'#{test_case}')
    for row in ans:
        print(*row)
