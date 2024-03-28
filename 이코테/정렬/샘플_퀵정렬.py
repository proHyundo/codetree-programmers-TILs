array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    rest = array[1::]
    print('rest : ', rest, ' | pivot : ', pivot)

    left = [x for x in rest if x <= pivot]
    right = [x for x in rest if x > pivot]
    print('left : ', left)
    print('right : ', right)
    print('=================')

    return quick_sort(left) + [pivot] + quick_sort(right)


print(quick_sort(array))
