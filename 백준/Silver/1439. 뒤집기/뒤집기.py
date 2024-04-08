_list = list(map(int, input()))
zero_cnt = 0
one_cnt = 0

if _list[0] == 0:
    zero_cnt += 1
else:
    one_cnt += 1

for i in range(1, len(_list)):
    if _list[i-1] != _list[i]:
        if _list[i] == 0:
            zero_cnt += 1
        else:
            one_cnt += 1

print(min(zero_cnt, one_cnt))