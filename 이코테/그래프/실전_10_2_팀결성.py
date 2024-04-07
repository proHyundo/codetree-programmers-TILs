# 문제 이름: 팀 결성
# 해결 날짜: 240404
# 소요 시간: 10분
# 시간 복잡도: [해결책의 시간 복잡도 삽입, 예: O(n), O(n^2) 등]
# 난이도: 중
# 문제 URL: [해당되는 경우 문제의 URL 삽입]
# 해결 접근 방식: [문제 해결에 접근한 방식을 간략히 설명. 여기에는 사용된 알고리즘, 데이터 구조 및 주목할 만한 최적화가 포함될 수 있음.]
# 코멘트: [문제나 해결책과 관련된 추가 코멘트나 비고 사항.]

N, M = map(int, input().split())

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find_parent(parent, num):
    if parent[num] != num:
        parent[num] = find_parent(parent, parent[num])
    return parent[num]

parent = [0] * (N+1)

for i in range(N+1):
    parent[i] = i


for _ in range(M):
    op, a, b = map(int, input().split())
    if op == 0:
        union_parent(parent, a, b)
    else:
        a_team = find_parent(parent, a)
        b_team = find_parent(parent, b)
        if a_team == b_team:
            print('YES')
        else:
            print('NO')


