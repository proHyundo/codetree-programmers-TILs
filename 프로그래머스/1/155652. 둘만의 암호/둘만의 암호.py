def solution(s, skip, index):

    s_list = list(map(ord, s))
    skip_list = list(map(ord, skip))
    z_ord = ord('z')
    a_ord = ord('a')
    
    for i, ele in enumerate(s_list):
        cnt = 0
        while cnt < index:
            ele += 1
            if ele > z_ord:
                ele = a_ord
            if ele not in skip_list:
                cnt += 1
        s_list[i] = ele
            
    
    
    return ''.join(map(chr, s_list))