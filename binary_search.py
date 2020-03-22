"""Реализация бинарного поиска в отсортированном массиве"""


def binary_search(a_list, element):
    """
    Binary search in sorted array
    :param a_list: array we searching an element in
    :param element: element needed to be found
    :return: [l, r] left and right bounds of the first occurrence of element
    """
    if len(a_list) == 0:
        return

    left = -1
    right = len(a_list)

    while right - left > 1:
        middle = (right + left) // 2
        if a_list[middle] < element:
            left = middle
        else:
            right = middle

    return [left, right]
