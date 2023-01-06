

def merge_sort(unordered_list):
    if len(unordered_list) <= 1:
        return unordered_list
    half_index = len(unordered_list) // 2
    left = merge_sort(unordered_list[:half_index])
    right = merge_sort(unordered_list[half_index:])
    return merge(left, right)


def merge(left, right):
    ordered_list = []
    while len(left) > 0 and len(right) > 0:
        if  left[0] <= right[0]:
            ordered_list.append(left.pop(0))
        else:
            ordered_list.append(right.pop(0))
    while len(left) > 0:
        ordered_list.append(left.pop(0))
    while len(right) > 0:
        ordered_list.append(right.pop(0))
    return ordered_list


