T = int(input())

for _ in range(T):
    F = int(input())
    dict1 = dict()
    dict2 = dict()
    cnt = 0
    for _ in range(F):
        name1, name2 = tuple(input().split())
        name1_flag = dict1.get(name1) if name1 in dict1 else False
        name2_flag = dict1.get(name2) if name2 in dict1 else False
        # dict 1 에 존재하는가?
        if not name1_flag and not name2_flag: # 둘다 처음 등장하는 값이라면
            cnt += 1
            dict1[name1] = dict1[name2] = cnt # dict1에 같은 cnt 으로 저장
            dict2[cnt] = [name1, name2]  # dict2에 같은 cnt를 key 값으로 저장
        elif name1_flag and name2_flag and name1_flag != name2_flag: # 둘다 존재하면서 다른 값 이라면 합쳐야 한다
            min_key = min(name1_flag, name2_flag)
            max_key = max(name1_flag, name2_flag) # dict2 에서 더 큰 값은 없애고, dict1 에서 더 작은 값으로 value를 재설정한다.
            pop_lst = dict2.pop(max_key)
            dict2[min_key] += pop_lst
            for ele in pop_lst:
                dict1[ele] = min_key
        elif name1_flag and not name2_flag: # name1만 값이 있는 경우, name1값으로 합친다.
            dict1[name2] = name1_flag
            dict2[name1_flag] += [name2]

        elif not name1_flag and name2_flag:
            dict1[name1] = name2_flag
            dict2[name2_flag] += [name1]

        print(len(dict2.get(dict1.get(name1))))