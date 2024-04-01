# 문제 이름: 부품찾기
# 해결 날짜: 240329
# 소요 시간: 14m
# 시간 복잡도: O(n log n)
# 난이도: 하
# 문제 URL: [해당되는 경우 문제의 URL 삽입]
# 해결 접근 방식: list in 연산자를 사용하면 O(n^2) 시간복잡도를, list 이진탐색을 사용하면 O(n log n) 시간복잡도를 가짐. 이진탐색으로 풀이.
# 코멘트: set 자료구조를 사용하면 O(n) 시간복잡도로 해결 가능. 계수정렬을 사용해도 O(n) 시간복잡도로 해결 가능.

N = int(input())
stocks = list(map(int, input().split()))
stocks.sort()
M = int(input())
orders = list(map(int, input().split()))


def binary_search(_list, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if _list[mid] == target:
        return mid
    elif _list[mid] > target:
        return binary_search(_list, target, start, mid - 1)
    else:
        return binary_search(_list, target, mid + 1, end)


for target in orders:
    if binary_search(stocks, target, 0, N - 1) is None:
        print('no', end=' ')
    else:
        print('yes', end=' ')

# set 자료구조 풀이

N = int(input())
stocks = set(map(int, input().split()))
M = int(input())
orders = list(map(int, input().split()))

for target in orders:
    print('yes' if target in stocks else 'no', end = ' ')