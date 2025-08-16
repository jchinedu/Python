def sort_array(source_array):
    odds = sorted([num for num in source_array if num % 2 != 0])

    result = []
    odd_index = 0
    for num in source_array:
        if num % 2 != 0:
            result.append(odds[odd_index])
            odd_index += 1
        else:
            result.append(num)

    return result
