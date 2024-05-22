L, C = map(int, input().split())
# 모음 > 1, 자음 > 2
vowels = {
    "a": True, "e": True, "i": True, "o": True, "u": True
}
words = sorted(list(input().split()))
ans = []


def dfs(n, start, lst):
    if n == L:
        # 정답 처리
        vowel = not_vowel = 0
        for a in lst:
            if a in vowels:
                vowel += 1
            else:
                not_vowel += 1
        if vowel > 0 and not_vowel > 1:
            ans.append(lst)
        return

    for s in range(start, C):
        dfs(n+1, s+1, lst + [words[s]])


dfs(0, 0, [])
for ele in ans:
    print(*ele, sep='')
