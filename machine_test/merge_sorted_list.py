def solution_one(list_a: list, list_b: list) -> list:
    merged_list = []

    i = 0
    j = 0

    while i < len(list_a) and j < len(list_b):
        if list_a[i] < list_b[j]:
            merged_list.append(list_a[i])
            i += 1
        else:
            merged_list.append(list_b[j])
            j += 1

    merged_list.extend(list_a[i:])
    merged_list.extend(list_b[j:])

    return merged_list
