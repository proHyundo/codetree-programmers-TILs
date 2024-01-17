
def solution(N, stages):
    # dic에 (스테이지 번호, 멈춘 사람 수)를 스테이지 번호 오름차순으로 정렬
    dic = dict()
    for stage in stages:
        dic[stage] = dic.get(stage, 0) + 1
    
    ans = [0 for _ in range(N+1)]
    user = len(stages)
    for i in range(N+1):
        c = dic.get(i, 0)
        if c != 0:
            ans[i] = c / user
            user -= c
            
    return sorted(range(1, N+1), key=lambda i: ans[i], reverse=True)
    
