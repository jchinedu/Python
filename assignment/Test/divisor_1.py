def divisor(numbers, divisor):
    if divisor == 0:
        return 'Divisor cannot be zero'
    
    result = [num for num in numbers if num % divisor == 0]
    if result:
        return result
    else:
        return 'No divisible number found'


print(divisor([11, 12, 21, 34, 56, 61], 0))
