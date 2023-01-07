import pytest

from searching.binary_search import binary_search, binary_search_recursive


def test_binary_search_returns_correct_result():
    search_list = [1, 2, 3, 4, 5, 6, 7]
    search_value = 1
    found_index = binary_search(search_list, search_value)
    assert found_index == 0


def test_binary_search_other_example_returns_correct_result():
    search_list = [1, 5, 9, 21, 100, 340, 1100, 2201, 8721]
    search_value = 8721
    found_index = binary_search(search_list, search_value)
    assert found_index == 8


def test_binary_search_missing_value_raises_valueerror_exception():
    search_list = [1, 2, 3, 4, 5, 6, 7]
    search_value = 9
    with pytest.raises(ValueError):
        binary_search(search_list, search_value)


def test_binary_search_recursive_returns_correct_result():
    search_list = [1, 2, 3, 4, 5, 6, 7]
    search_value = 1
    found_index = binary_search_recursive(search_list, search_value)
    assert found_index == 0


def test_binary_search_recursive_other_example_returns_correct_result():
    search_list = [1, 5, 9, 21, 100, 340, 1100, 2201, 8721]
    search_value = 8721
    found_index = binary_search_recursive(search_list, search_value)
    assert found_index == 8


def test_binary_search_recursive_missing_value_raises_valueerror_exception():
    search_list = [1, 2, 3, 4, 5, 6, 7]
    search_value = 9
    with pytest.raises(ValueError):
        binary_search_recursive(search_list, search_value)