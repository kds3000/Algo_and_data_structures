"""Реализация быстрой сортировки с использованием доп. памяти и без"""


def quick_sort_memory(a_list):
    """Simple quick sort"""
    if len(a_list) <= 1:
        return
    mid_index = len(a_list) // 2
    pivot = a_list[mid_index]
    first_half = []
    second_half = []
    middle = []
    for element in a_list:
        if element < pivot:
            first_half.append(element)
        elif element == pivot:
            middle.append(element)
        else:
            second_half.append(element)
    quick_sort_memory(first_half)
    quick_sort_memory(second_half)
    result = first_half + middle + second_half
    for i in range(len(result)):
        a_list[i] = result[i]


def quick_sort(a_list, start, finish):
    """No additional memory required"""
    if start >= finish:
        return

    mid_index = start + (finish - start) // 2
    left_index = start
    right_index = finish
    pivot = a_list[mid_index]

    while left_index <= right_index:
        while a_list[left_index] < pivot:
            left_index += 1
        while a_list[right_index] > pivot:
            right_index -= 1
        if left_index <= right_index:
            a_list[left_index], a_list[right_index] = a_list[right_index], a_list[left_index]
            left_index += 1
            right_index -= 1

    quick_sort(a_list, start, right_index)
    quick_sort(a_list, left_index, finish)
