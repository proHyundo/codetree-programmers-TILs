from itertools import product

def solution(word):
    _list = []
    count = 0
    answer = 0
    for i in range(1, 6):
        for t in product(['A', 'E', 'I', 'O', 'U'], repeat = i):
            _list.append(''.join(t))

    _list.sort()
    
    for t in _list:
        count += 1
        if word == t:
            answer = count
            break

    return answer