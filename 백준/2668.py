N = int(input())
dic = dict()
for i in range(1, N+1):
    n = int(input())
    dic[i] = n

answer = set()
cnt = 0
for key, value in dic.items():
    if key == value:
        cnt += 1
        answer.add(value)
    else:
        if dic.get(value) == key:
            cnt += 1
            answer.add(value)



print(cnt)
print(*sorted(answer),sep='\n')