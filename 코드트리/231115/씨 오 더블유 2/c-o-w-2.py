n = int(input())
string = list(input())
ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if string[i] == 'C' and string[j] == 'O' and string[k] == 'W':
                ans += 1

print(ans)