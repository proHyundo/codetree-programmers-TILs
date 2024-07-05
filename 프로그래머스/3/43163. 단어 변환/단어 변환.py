import sys


def solution(begin, target, words):
    answer = sys.maxsize
    length = len(words)
    v = [False] * length
    if target not in words:
        return 0

    def check_diff(r, w):
        cnt = 0
        for e1, e2 in zip(list(r), list(w)):
            if e1 != e2:
                cnt += 1
            if cnt > 1:
                break
        return True if cnt == 1 else False

    def dfs(cnt, rst):
        nonlocal answer
        if cnt > answer:
            return
        if rst == target:
            answer = min(answer, cnt)
            return

        for i in range(length):
            if not v[i] and check_diff(rst, words[i]):
                v[i] = True
                dfs(cnt + 1, words[i])
                v[i] = False

    dfs(0, begin)

    return answer if answer != sys.maxsize else 0