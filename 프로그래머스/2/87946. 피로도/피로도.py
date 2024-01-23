from itertools import permutations
def solution(k, dungeons):
    dun_size = len(dungeons)
    answer = -1
    
    for order in permutations(range(1, dun_size+1), dun_size):
        pass_cnt = 0
        hp = k
        for index in order:
            if dungeons[index-1][0] <= hp: # 최소필요피로도 만족
                # print(order, index, hp, pass_cnt)
                pass_cnt += 1
                hp -= dungeons[index-1][1]
            else:
                break
        answer = max(answer, pass_cnt)
            
    
    return answer