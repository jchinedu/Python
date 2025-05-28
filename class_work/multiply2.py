def multiple(number1, number2):
    negative_result = (number1 < 0) ^ (number2 < 0)
    
  
    number1 = abs(number1)
    number2 = abs(number2)

    scale = 1000
    n1 = int(number1 * scale)
    n2 = int(number2 * scale)
    
   
    result = 0
    for _ in range(n1):
        result += n2
    
  
    result = result / (scale * scale)

   
    if negative_result:
        result = -result
    
    return result




print(multiple(2.4, 5.4))
