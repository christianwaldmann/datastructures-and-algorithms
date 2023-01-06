

def insertion_sort(unordered_list):
    for i in range(1, len(unordered_list)):
        element_to_insert = unordered_list[i]
        j = i
        while j > 0 and unordered_list[j - 1] > element_to_insert:
            unordered_list[j] = unordered_list[j - 1]
            j -= 1
        unordered_list[j] = element_to_insert
    return unordered_list
