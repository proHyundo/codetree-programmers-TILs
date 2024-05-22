L, C = map(int, input().split())
vowels = {
    "a": True, "e": True, "i": True, "o": True, "u": True
}
words = sorted(list(input().split()))
ans = []

# multi tree
def dfs(n, start, lst):
    if n == L:
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


# binary tree
def dfs_binary_tree(n, cnt, lst):
    # 가지치기
    if cnt > L:
        return
    # 종료조건
    if n == C:
        if cnt == L:
            vowel = not_vowel = 0
            for a in lst:
                if a in vowels:
                    vowel += 1
                else:
                    not_vowel += 1
            if vowel > 0 and not_vowel > 1:
                ans.append(lst)
        return

    dfs_binary_tree(n+1, cnt+1, lst + [words[n]])
    dfs_binary_tree(n+1, cnt, lst)


dfs_binary_tree(0, 0, [])
for ele in ans:
    print(*ele, sep='')

# 해설 영상 팁
# 1) 문자를 출력할 것이니, lst 대신 문자 타입으로 받는다.
# 2) 모음의 개수를 매개변수로 받는다.
# 3) 자음 개수 = L - 모음 개수