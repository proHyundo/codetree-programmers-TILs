a = list(input())
for i, ele in enumerate(a):
    if ele == '0':
        a[i] = '1'
        break

string = ''.join(a)

print(int('0b'+string, 2))