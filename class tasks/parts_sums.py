def parts_sums(ls):
    result = [0] * (len(ls) + 1)  
    for i in range(len(ls) - 1, -1, -1):  
        result[i] = result[i + 1] + ls[i]
    return result
