#write a script that swaps two integers without using a temporary variable
#input = a, b = 5, 10
#output = a, b = 10,5

a, b = 5,10

a = a + b
b = a - b
a = a - b

print(a,b)