

def linear_search(search_list, search_value):
    for i, element in enumerate(search_list):
        if element == search_value:
            return i
    raise ValueError(f"Element {search_value} not found in list {search_list}")
