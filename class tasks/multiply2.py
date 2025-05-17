def multiply(number1, number2):
    negative = (number1 < 0) != (number2 < 0)
    number1 = abs(number1)
    number2 = abs(number2)

    scale = 10 ** 4
    float_number1 = int(number1 * scale)
    float_number2 = int(number2 * scale)
    
    result = 0
    for i in range(float_number2):
        result += float_number1
    
    result = result / (scale ** 2)
    
    if negative:
      result = -result
    if result == int(result):
      return int(result)
    return result







