"""Реализация сортировки пузырьком, сортировки вставками, сортировки выбором"""
from test_for_sort_algo import test_func


def bubble_sort(a_list):
    for bypass in range(1, len(a_list)):
        permutations = 0
        for i in range(len(a_list) - bypass):
            if a_list[i] > a_list[i+1]:
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
                permutations += 1
        if permutations == 0:
            break


def selection_sort(a_list):
    for start in range(0, len(a_list)-2):
        _min = start
        for j in range(start, len(a_list)):
            if a_list[_min] > a_list[j]:
                _min = j
        if _min != start:
            a_list[start], a_list[_min] = a_list[_min], a_list[start]


def insert_sort(a_list):
    for start in range(1, len(a_list)):
        k = start
        while k > 0 and a_list[k] < a_list[k-1]:
            a_list[k], a_list[k-1] = a_list[k-1], a_list[k]
            k -= 1


def main():
    test_func(selection_sort)
