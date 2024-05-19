string = input()
ans = 0

for i in range(len(string)-1):
    if string[i] == '(' and string[i+1] == '(':
        if i + 3 <= len(string):
            for j in range(i + 2, len(string)-1):
                if string[j] == ')' and string[j+1] == ')':
                    ans += 1

print(ans)