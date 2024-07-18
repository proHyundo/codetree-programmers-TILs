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