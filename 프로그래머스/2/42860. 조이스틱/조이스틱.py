def find_min_change(input_name):
    cnt = 0
    for n in input_name:
        cnt += min(ord(n) - 65, 91 - ord(n))
    return cnt


def solution(name):
    answer = 0
    moved = 9999999

    # 좌/우 총 이동 횟수 최소 값 구하기
    target_cnt = len(name) - list(name).count('A')
    visited = [False] * len(name)

    def move(direct, c):
        if direct == 'L':
            for i in range(20):
                if 'A' != name[c - i] and not visited[c-i]:
                    return c - i, i

        if direct == 'R':
            for i in range(20):
                if 'A' != name[c + i] and not visited[c+i]:
                    return c + i, i

    def dfs(n, cnt, cur):
        nonlocal moved
        # A가 아닌 것들을 모두 방문하면 종료
        if n == target_cnt:
            moved = min(moved, cnt)
            return

        # 좌로 이동
        l_nxt, l_cnt = move('L', cur)
        visited[l_nxt] = True
        dfs(n+1, cnt + l_cnt, l_nxt)
        visited[l_nxt] = False

        # 우로 이동
        r_nxt, r_cnt = move('R', cur)
        visited[r_nxt] = True
        dfs(n+1, cnt + r_cnt, r_nxt)
        visited[r_nxt] = False

    dfs(0, 0, 0)
    answer += moved
    # 문자 변경 총 횟수 구하기
    answer += find_min_change(name)

    return answer