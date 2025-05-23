def product(*args):
    result = 1
    for number in args:
        result *= number
    return result
#print(product(2, 3, 4))          
print(product(5))               
#print(product(1, 2, 3, 4, 5))   
#print(product())                
