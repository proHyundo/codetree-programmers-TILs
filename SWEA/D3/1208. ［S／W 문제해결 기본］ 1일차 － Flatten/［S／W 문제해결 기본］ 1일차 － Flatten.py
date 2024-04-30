T = 10
for test_case in range(1, T+1):
    dump_cnt = int(input())
    boxes = list(map(int, input().split()))
    boxes.sort()
    if boxes[0] == boxes[99] or boxes[99] - boxes[0] == 1:
        print(f'#{test_case}', boxes[99] - boxes[0])
        break
    for _ in range(dump_cnt):
        min_index = 0
        max_index = 99
        boxes[0] += 1
        boxes[99] -= 1
        # 앞 부터 부분 정렬
        while boxes[min_index] > boxes[min_index+1]:
            boxes[min_index], boxes[min_index+1] = boxes[min_index+1], boxes[min_index]
            min_index += 1
        # 뒤 부터 부분 정렬
        while boxes[max_index] < boxes[max_index-1]:
            boxes[max_index], boxes[max_index - 1] = boxes[max_index - 1], boxes[max_index]
            max_index -= 1

    print(f'#{test_case}',boxes[99] - boxes[0])