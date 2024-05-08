# 이진트리로 풀이하였다. 멀티트리로도 풀이 가능하다. 참고 링크 : https://youtu.be/WUq13ACJmB8
N, M = map(int, input().split())
ans = []


def dfs(n, cnt, lst):
    if n > N:
        if cnt == M:  # len(lst)의 시간복잡도는 O(1) 이다. 따라서 cnt 변수를 사용하지 않아도 된다.
            ans.append(lst)
        return

    dfs(n+1, cnt+1, lst + [n])
    dfs(n+1, cnt, lst)


dfs(1, 0, [])
for ele in ans:
    print(*ele)
