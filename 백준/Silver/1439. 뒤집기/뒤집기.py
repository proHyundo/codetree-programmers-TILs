_list = list(map(int, input()))

one_group = []
zero_group = []
zero_result = 0
one_result = 0

for n in _list:
    if n == 0:
        zero_group.append(n)
    elif n != 0 and len(zero_group) > 0:
        zero_result += 1
        zero_group.clear()

    if n == 1:
        one_group.append(n)
    elif n != 1 and len(one_group) > 0:
        one_result += 1
        one_group.clear()


if len(zero_group) > 0:
    zero_result += 1

if len(one_group) > 0:
    one_result += 1

print(min(zero_result, one_result))
