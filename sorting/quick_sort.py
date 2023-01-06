

def quick_sort(unordered_list):
    return quick_sort_helper(unordered_list, 0, len(unordered_list) - 1)


def quick_sort_helper(unordered_list, left_index, right_index):
    if left_index >= right_index:
        return unordered_list
    i = partition(unordered_list, left_index, right_index)
    quick_sort_helper(unordered_list, left_index, i - 1)
    quick_sort_helper(unordered_list, i + 1, right_index)
    return unordered_list


def partition(unordered_list, left_index, right_index):
    i = left_index
    j = right_index - 1
    pivot_element = unordered_list[right_index]
    while i < j:
        while i < j and unordered_list[i] <= pivot_element:
            i += 1
        while j > i and unordered_list[j] > pivot_element:
            j -= 1
        if unordered_list[i] > unordered_list[j]:
            unordered_list[i], unordered_list[j] = unordered_list[j], unordered_list[i]
    if unordered_list[i] > pivot_element:
        unordered_list[i], unordered_list[right_index] = unordered_list[right_index], unordered_list[i]
    else:
        i = right_index
    return i

