def solution(numbers):
    answer = []
    for num in numbers:
        b = bin(num)[2:]
        size, length = len(b), 0
        if size == 1:
            pass
        elif size <= 3:
            length = 3 - size
        elif size <= 7:
            length = 7 - size
        elif size <= 15:
            length = 15 - size
        elif size <= 31:
            length = 31 - size
        elif size <= 63:
            length = 63 - size

        b = '0' * length + str(b)

        # 루트가 없으면 표현 불가
        if b[len(b)//2] == '0':
            answer.append(0)
            continue

        def dfs(target_node, move_cnt):
            if target_node % 2 == 1: # 리프노드 도달
                return True
            # 지금 내가 0 이라면
            if b[target_node-1] == '0':
                # 좌우 자식 노드도 0 이어야 하고
                if b[target_node + move_cnt//2 -1] == '1' or b[target_node - move_cnt//2 -1] == '1':
                    return False
            # 지금 내가 1 이라면
            # 그냥 자식 노드로 target 넘기면 됨
            right_result = dfs(target_node + move_cnt // 2, move_cnt // 2)
            left_result = dfs(target_node - move_cnt // 2, move_cnt // 2)
            return right_result and left_result

        result = dfs(len(b)//2 + 1, len(b)//2 + 1)

        answer.append(1) if result else answer.append(0)
    return answer