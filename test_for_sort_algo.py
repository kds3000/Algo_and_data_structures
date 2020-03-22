"""Sort testing module"""


def test_func(sort_func):
    """sort algo simple test function"""
    list1 = [5, 3, 45, -5, 0, 16, 34, 67]
    list2 = [8, 8, 6, 6, 6, 5, 4, 5, 6, 5, 4, 0, 0, 0]
    list3 = [3.14, 6.54, -6.56, 76, 88]
    list4 = [i for i in range(19, -1, -1)]
    lists = (list1, list2, list3, list4)

    result1 = [-5, 0, 3, 5, 16, 34, 45, 67]
    result2 = [0, 0, 0, 4, 4, 5, 5, 5, 6, 6, 6, 6, 8, 8]
    result3 = [-6.56, 3.14, 6.54, 76, 88]
    result4 = [i for i in range(20)]
    results = (result1, result2, result3, result4)

    for (a_list, result) in zip(lists, results):
        try:
            sort_func(a_list)
            assert a_list == result
        except AssertionError:
            print('Test failed')
            print(a_list)
        else:
            print('Test passed')
