import pytest

from searching.linear_search import linear_search


def test_linear_search_returns_correct_result():
    search_list = [4, 2, 6, 1, 7, 3, 5]
    search_value = 1
    found_index = linear_search(search_list, search_value)
    assert found_index == 3


def test_linear_search_for_objects_returns_correct_result():
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __eq__(self, other):
            return self.x == other.x and self.y == other.y

    p1 = Point(1, 3)
    p2 = Point(5, 2)
    p3 = Point(3, 4)
    p4 = Point(1, 0)
    search_list = [p1, p2, p3, p4]
    search_value = Point(1, 0)
    found_index = linear_search(search_list, search_value)
    assert found_index == 3


def test_linear_search_missing_value_raises_valueerror_exception():
    search_list = [4, 2, 6, 1, 7, 3, 5]
    search_value = 9
    with pytest.raises(ValueError):
        linear_search(search_list, search_value)
