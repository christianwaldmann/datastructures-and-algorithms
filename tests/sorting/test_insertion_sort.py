from sorting.insertion_sort import insertion_sort


def test_insertion_sort_unordered_list_returns_correct_result():
    unordered_list = [4, 2, 6, 1, 7, 3, 5]
    ordered_list = insertion_sort(unordered_list)
    assert ordered_list == [1, 2, 3, 4, 5, 6, 7]


def test_insertion_sort_empty_list_returns_correct_result():
    unordered_list = []
    ordered_list = insertion_sort(unordered_list)
    assert ordered_list == []


def test_insertion_sort_list_with_only_zeros_returns_correct_result():
    unordered_list = [0, 0, 0]
    ordered_list = insertion_sort(unordered_list)
    assert ordered_list == [0, 0, 0]


def test_insertion_sort_ordered_list_returns_correct_result():
    unordered_list = [1, 2, 3, 4, 5, 6, 7]
    ordered_list = insertion_sort(unordered_list)
    assert ordered_list == [1, 2, 3, 4, 5, 6, 7]


def test_insertion_sort_list_reversed_list_returns_correct_result():
    unordered_list = [7, 6, 5, 4, 3, 2, 1]
    ordered_list = insertion_sort(unordered_list)
    assert ordered_list == [1, 2, 3, 4, 5, 6, 7]


def test_insertion_sort_list_with_same_elements_returns_correct_result():
    unordered_list = [5, 5, 5]
    ordered_list = insertion_sort(unordered_list)
    assert ordered_list == [5, 5, 5]


def test_insertion_sort_list_with_negative_values_returns_correct_result():
    unordered_list = [-1, -3, 5, -2, 7]
    ordered_list = insertion_sort(unordered_list)
    assert ordered_list == [-3, -2, -1, 5, 7]
