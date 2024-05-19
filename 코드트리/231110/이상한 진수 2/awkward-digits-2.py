a = list(input())
found_flag = False

for i, ele in enumerate(a):
    if ele == '0':
        a[i] = '1'
        found_flag = True
        break

if found_flag:
    string = ''.join(a)
else:
    a[-1] = '0'
    string = ''.join(a)

print(int('0b'+string, 2))