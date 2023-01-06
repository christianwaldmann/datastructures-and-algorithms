

def bubble_sort(unordered_list):
    for i in range(len(unordered_list)):
        for j in range(len(unordered_list) - i - 1):
            if unordered_list[j] > unordered_list[j + 1]:
                unordered_list[j + 1], unordered_list[j] = unordered_list[j], unordered_list[j + 1]
    return unordered_list
