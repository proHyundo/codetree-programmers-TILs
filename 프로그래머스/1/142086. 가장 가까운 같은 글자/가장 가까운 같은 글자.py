def solution(s):
    answer = []
    dic = {}
    for i, ele in enumerate(s):
        # print(i+1, ele, dic.get(ele, -1))
        temp = dic.get(ele, -1)
        if temp == -1:
            answer.append(-1)
        else:
            answer.append(i+1-temp)
            
        dic[ele] = i+1
    return answer