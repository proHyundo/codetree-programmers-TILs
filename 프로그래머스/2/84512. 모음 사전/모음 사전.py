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

    for index, target, in enumerate(_lst):
        if word == target:
            answer = index
            break
    return answer