_list = list(map(int, input()))

length = len(_list)
tempA = sum(_list[:length//2])
tempB = sum(_list[length//2:])

if tempA == tempB:
    print('LUCKY')
else:
    print('READY')