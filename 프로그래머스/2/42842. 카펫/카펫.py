def solution(brown, yellow):
    by = brown + yellow
    # 가로의 길이를 1부터 by까지 순회
    for i in range(1, by+1):
        # 가로세로가 정수이면서, 가로의 길이가 더 길면서, 노란색의 개수가 가로-2 * 세로-2 조건을 만족할때
        if (by % i == 0) and (i >= by // i) and (yellow == (i-2)*(by//i-2)):
            return [i, by//i]
