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


def count_times_with_three(N):
    # 0 ~ N 시간 중 '3' 이 들어간 시간의 개수
    hours_with_three = sum(1 for hour in range(N + 1) if '3' in str(hour))
    print(hours_with_three)

    # 3을 포함하는 분 또는 초 개수 : 03, 13, 23, 30-39, 43, 53
    minutes_with_three = 15
    seconds_with_three = 15

    # 전체 시 : 0부터 세니까 1 더함
    total_hours = N + 1

    # '3'이 들어간 시간은 전체 다 카운트
    total_with_hour_three = hours_with_three * 60 * 60

    # '3'이 들어 가지 않은 시간 = 전체 시 - '3'이 들어간 시
    hours_without_three = total_hours - hours_with_three

    # '3'이 들어가지 않은 시간은 일부만 카운트
    total_with_minute_three = hours_without_three * minutes_with_three * 60
    minutes_without_three = 60 - minutes_with_three
    total_with_second_three = hours_without_three * minutes_without_three * seconds_with_three

    # Total count
    total = total_with_hour_three + total_with_minute_three + total_with_second_three

    return total

print(count_times_with_three(n))
