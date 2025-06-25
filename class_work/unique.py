def unique_in_order(sequence):
    result = []
    prev = object()  # Dummy value that won't match anything

    for item in sequence:
        if item != prev:
            result.append(item)
            prev = item

    return result
