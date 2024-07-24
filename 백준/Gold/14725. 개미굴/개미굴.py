N = int(input()) # 먹이의 개수
cave = dict()

for _ in range(N):
    lst = list(input().split())

    if not lst[1] in cave:
        cave[lst[1]] = dict()
    parent = cave.get(lst[1])

    for i in range(2, len(lst)):
        if not lst[i] in parent:
            parent[lst[i]] = dict()
        parent = parent.get(lst[i])


def recurse_dict(d, depth):
    for key, value in sorted(d.items()):
        print('--' * depth + str(key))
        if isinstance(value, dict):
            recurse_dict(value, depth + 1)


recurse_dict(cave, 0)
