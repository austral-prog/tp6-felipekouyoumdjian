def remove_elements(list_to_remove_elements):
    length = len(list_to_remove_elements)
    if length == 0:
        return []
    elif length < 5:
        return list_to_remove_elements[1:]
    elif length == 5:
        return list_to_remove_elements[1:4]
    else:
        return list_to_remove_elements[1:4] + list_to_remove_elements[6:]
print(remove_elements(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'Blue']))


def add_elements(list_to_add_elements):
    return ["Pink"] + list_to_add_elements + ["Yellow"]
print(add_elements(['Red', 'Green', 'White', 'Black']))


def is_empty(list_to_check):
    if len(list_to_check) == 0:
        return True
    return False
print(is_empty([]))

def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) < 3 or len(list_to_compare2) < 3:
        return False
    else:
        if list_to_compare1[2] == list_to_compare2[2]:
            return True
        return False
print(check_lists(['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White'], 
                  ['Red', 'Green', 'Yellow', 'White', 'Black', 'Pink']))

def list_of_lists(list_of_lists_to_modify):
    new_list = [list_of_lists_to_modify[0][:2], list_of_lists_to_modify[1][1:4], list_of_lists_to_modify[2][-2:]]
    return new_list
print(list_of_lists([[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]))