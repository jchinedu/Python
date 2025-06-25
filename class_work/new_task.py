from random import randint
numbers = []
def random_number():
    for i in range(10):
        number = randint(1,51)
        numbers.append(number)
        return numbers


def length_of_list(numbers):
    count = 0
    for number in numbers:
        count +=1
    return count

def sum_elements_at_even_positions(numbers):
    count = 0
    index = 0
    for number in numbers:
        if index % 2 == 0:
            count += number
        index += 1
    return count





def sum_odd_elements_at_odd_positions(numbers):
    index = 0
    count = 0
    for number in numbers:
        if index % 2 == 1:
            count += number
        index += 1
    return count



def multiply_all_elements_at_every_third_positions(numbers):
    count = 1
    index = 0
    for number in numbers:
        if (index+1) % 3 == 0:
            count *= number
        index += 1
    return count

def calculate_the_average_of_all_elements_in_the_list(numbers):
    count = 0
    total = 0
    for number in numbers:
        total += number
    for number in numbers:
        count = count + 1
    average = total / count
    return average




