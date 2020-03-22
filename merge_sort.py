"""Реализация сортировки слиянием без использования дополнительной памяти"""


def merge_sort(a_list, start, finish):
    if start >= finish:
        return
    middle = start + (finish - start) // 2
    merge_sort(a_list, start, middle)
    merge_sort(a_list, middle+1, finish)
    merge(a_list, start, middle, finish)


def merge(a_list, start, middle, finish):
    tmp = []
    first = start
    second = middle + 1

    while first <= middle and second <= finish:
        if a_list[first] <= a_list[second]:
            tmp.append(a_list[first])
            first += 1
        else:
            tmp.append(a_list[second])
            second += 1

    while first <= middle:
        tmp.append(a_list[first])
        first += 1
    while second <= finish:
        tmp.append(a_list[second])
        second += 1

    for i in range(start, middle + 1):
        a_list[i] = tmp[i-start]
    for i in range(middle + 1, finish + 1):
        a_list[i] = tmp[i-start]

