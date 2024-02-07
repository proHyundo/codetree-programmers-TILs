def solution(s):
    _list = list(map(int, s.split(' ')))
    return str(min(_list)) + ' ' + str(max(_list))
            