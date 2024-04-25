# 문제 이름: 모함가 길드
# 해결 날짜: 240408
# 소요 시간: 34분 -> 8분
# 시간 복잡도: O(n)
# 난이도: 중
# 문제 URL: [해당되는 경우 문제의 URL 삽입]
# 해결 접근 방식: 최적해를 구하지 못한 잘못된 풀이. 다시 풀어볼 것.
# 코멘트: 다시 풀었을 때 stack 을 이용했음. 그러나 단순히 stack의 길이만 중요하다면 굳이 스택 그 자체가 필요하진 않았음.

# 2번째 풀이
_list = list(map(int, input().split()))
_list.sort()
stack = []
ans = 0

for i in _list:
    stack.append(i)
    if i <= len(stack):
        ans += 1
        stack.clear()

print(ans)