# 문제 이름: [문제 이름 삽입]
# 해결 날짜: [YY-MM-DD 형식으로 날짜 삽입]
# 소요 시간: [문제를 해결하는데 걸린 시간 삽입, 예: 45분]
# 시간 복잡도: [해결책의 시간 복잡도 삽입, 예: O(n), O(n^2) 등]
# 난이도: [난이도 수준 삽입, 예: 상, 중, 하]
# 문제 URL: [해당되는 경우 문제의 URL 삽입]
# 해결 접근 방식: [문제 해결에 접근한 방식을 간략히 설명. 여기에는 사용된 알고리즘, 데이터 구조 및 주목할 만한 최적화가 포함될 수 있음.]
# 코멘트: [문제나 해결책과 관련된 추가 코멘트나 비고 사항.]

n = int(input())
build_frame = [
    list(map(int, input().split())) for _ in range(n)
]

pillars = set()
floors = set()
result = [[]]

def in_range(x, y, type):
    if type == 0: #기둥
        if 0 <= x <= n and 0 <= y < n:
            return True
    else: # 보
        if 0 <= x <= n and 1 <= y <= n:
            return True
    return False


def is_possible_pillar(x, y):
    if y == 0 or (x, y) in pillars or (x, y) in floors:
        return True
    return False

for command in build_frame:
    x, y, a, b = command[0],command[1],command[2],command[3] 
    if a == 0: # 기둥
        if b == 0: # 설치
            # n 격자 내부 인지, # 바닥이거나 보 또는 기둥 위에 설치하는지
            if in_range(x, y, 0) and is_possible_pillar(x, y):
                result.append([x, y, 0])
                pillars.add((x, y))
                pillars.add((x, y+1))
        else: # 삭제
            if (x, y+1) not in pillars:
                pass

    if a == 1: # 보
        if b == 0:  # 설치
            pass
        else:  # 삭제
            # 보 한쪽 끝이 기둥 위에 있거나, 양쪽 끝이 다른 보와 연결됨
            pass

