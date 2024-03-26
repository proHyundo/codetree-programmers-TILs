# 문제 이름: 시각
# 해결 날짜: 240326
# 소요 시간: 10m 50s
# 시간 복잡도: O(n^3)
# 난이도: 하
# 문제 URL: [해당되는 경우 문제의 URL 삽입]
# 해결 접근 방식: 시분초 3중 for문을 사용했음.
# 코멘트: if 문을 str() 함수를 사용하도록 개선

n = int(input())
ans = 0

for h in range(0, n+1):
    for m in range(0, 60):
        for s in range(0, 60):
            if '3' in str(h) + str(m) + str(s):
                ans += 1


print(ans)
