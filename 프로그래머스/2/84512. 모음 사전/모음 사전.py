# 첫 번째 풀이 : 라이브러리 사용
from itertools import product

def solution(word):
    _list = []
    answer = 0
    for i in range(1, 6):
        for t in product(['A', 'E', 'I', 'O', 'U'], repeat = i):
            _list.append(''.join(t))

    _list.sort()

    for index, t in enumerate(_list):
        if word == t:
            answer = index + 1
            break

    return answer

# 두 번째 풀이 : 직접 구현
lst = set()
chars = ['', 'A', 'E', 'I', 'O', 'U']

def dfs(n, word):
    if n == 5:
        lst.add(word)
        return

    for c in chars:
        dfs(n+1, word + c)


def solution(word):
    answer = 0
    dfs(0, '')
    _lst = sorted(list(lst))
    print(lst)

    for index, target, in enumerate(_lst):
        if word == target:
            answer = index
            break
    return answer