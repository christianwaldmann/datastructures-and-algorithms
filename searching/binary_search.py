

def binary_search(ordered_list, search_value):
    start_index = 0
    end_index = len(ordered_list) - 1
    while start_index <= end_index:
        half_index = (start_index + end_index) // 2
        if search_value == ordered_list[half_index]:
            return half_index
        elif search_value < ordered_list[half_index]:
            end_index = half_index - 1
        else:
            start_index = half_index + 1
    raise ValueError(f"Element {search_value} not found in list {ordered_list}")


def binary_search_recursive(ordered_list, search_value):
    return binary_search_recursive_helper(ordered_list, search_value, 0, len(ordered_list) - 1)


def binary_search_recursive_helper(ordered_list, search_value, start_index, end_index):
    if (end_index - start_index) <= 0:
        if ordered_list[start_index] == search_value:
            return start_index
        raise ValueError(f"Element {search_value} not found in list {ordered_list}")
    half_index = (start_index + end_index) // 2
    if search_value == ordered_list[half_index]:
        return half_index
    elif search_value < ordered_list[half_index]:
        return binary_search_recursive_helper(ordered_list, search_value, start_index, half_index - 1)
    else:
        return binary_search_recursive_helper(ordered_list, search_value, half_index + 1, end_index)
