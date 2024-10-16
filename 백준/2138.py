# 000 > 111 : 1
# 000 > 010 : 3
# 000 > 011 : 1
# 000 > 110 : 1
# 000 > 101 : 2
# 000 > 100 :


# 000
# 110       011         111
# 101 001   101 100     001 100
# 010

N = int(input())
before = list(map(int, input()))
after = list(map(int, input()))

change_cnt = 0
for i in range(1, N):
    if before[i] == after[i]:
        continue

    for j in range(i-1, i+2+1):
        if 0 <= j < N:
            before[j] = 1 - before[j]

    change_cnt += 1


print(before)
print(after)
print(change_cnt)