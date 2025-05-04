print('Number spacing')

Number = int(input('Enter any five digit  number: '))
number1 =float(Number //10000)
number2 =float((Number //1000) % 10)
number3 = float ((Number //100) % 10)
number4 = float ((Number //10) % 10)
number5 = float(Number % 10)

print(f"{int(number1)}   {int(number2)}   {int(number3)}   {int(number4)}   {int(number5)}")
                                                                                                                                                                                                                                                                                                                         
