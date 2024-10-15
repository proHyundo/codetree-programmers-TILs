T = int(input())


def dfs(n, string):
    global N, lst
    if n == N:
        if eval(string.replace(' ', '')) == 0:
            lst.append(string)
        return

    dfs(n + 1, string + '+' + str(arr[n])) # 덧셈
    dfs(n + 1, string + '-' + str(arr[n])) # 뺄셈
    dfs(n + 1, string + ' ' + str(arr[n]))  # 공백


for _ in range(T):
    N = int(input())
    arr = [i for i in range(1, N+1)]
    lst = []
    dfs(1, str(arr[0]))
    lst.sort()

    for a in lst:
        print(a)
    print()