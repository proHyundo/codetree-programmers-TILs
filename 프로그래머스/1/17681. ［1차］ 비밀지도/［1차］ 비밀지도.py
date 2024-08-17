def solution(n, arr1, arr2):
    answer = []
    s_len = '0'+str(n)
    for e1, e2 in zip(arr1, arr2):
        temp = ''
        b1 = format(int(bin(e1)[2:]), s_len)
        b2 = format(int(bin(e2)[2:]), s_len)
        
        for w1, w2 in zip(b1, b2):
            if w1 == w2 and w1 == '0':
                temp += ' '
            else:
                temp += '#'
        answer.append(temp)

    return answer