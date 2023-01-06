import math


def selection_sort(unordered_list):
    for i in range(len(unordered_list) - 1):
        minValue = math.inf
        minIndex = i
        for j in range(i, len(unordered_list)):
            if unordered_list[j] < minValue:
                minValue = unordered_list[j]
                minIndex = j
        unordered_list[i], unordered_list[minIndex] = unordered_list[minIndex], unordered_list[i]
    return unordered_list
