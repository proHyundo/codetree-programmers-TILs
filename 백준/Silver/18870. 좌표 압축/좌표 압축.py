N = int(input())
arr = list(map(int, input().split()))
sarr = sorted(list(set(arr)))

def binary_search(target):
    left = 0
    right = len(sarr) - 1
    mid = 0
    while left <= right:
        mid = (left + right) // 2
        if sarr[mid] == target:
            return mid
        elif sarr[mid] < target:
            left = mid + 1
        elif sarr[mid] > target:
            right = mid - 1
    return mid


for ele in arr:
    print(binary_search(ele), end=' ')
