
def function():
    lists = [10, 20, 30, 40, 50]
    print(lists[2])


def function2():
    colors = ['red', 'green', 'blue']
    colors.remove('blue')
    colors.insert(2, 'yellow')
    print(colors)




def function3():
    colors = ['red', 'green', 'blue']
    colors.append('purple')
    print(colors)

def function4():
    list = [1,2,3,4,5]
    list.remove(3)
    print(list)
def function5():
    list = ['Alice', 'bob', 'Charlie']
    for name in list:
        print(len(name))
def function6():
    list = [4,1,3,9,2]
    list.sort()
    print(list)

def function7():
    list = [1,2,3,4,5,6,7,8,9,10]
    for number in list:
        if number % 2 != 0:
            list.remove(number)
    print(list)

def function8():
    list = [1,2,3]
    list2 = [4,5,6]

    list3 =list + list2
    print(list3)

def function9():
    lists = ["lamb", "kit", "yam", "kings", "dogs", "man"]
    word = []
    for names in lists:
        if len(names) > 3:
            word.append(names)
    print(word)

def unpack_collection(collection):
    result = (0,0,0,0)
    for index in range(4):
        result[index] += collection[index]
    return result


my_list = [1,2,3,4,5,6,7,8,9,10]



def unparking_collection(collection):
    first_number, second_number, third_number, four_number = collection
    return first_number, second_number, third_number, other
    print(unparking_collection(my_list))


def slicing_collection(collection):
    return collection[0: 8: 1]

def sort_collection(collection):
    number.sort(reverse=True)
    return collection


def filter_with_lambda(my_list):
    return list(filter(lambda x: x % 2 == 1, my_list))
    print(filter_with_lambda(my_list))
 
#function7()
#function8()
#function9()
my_list = [1,2,3,4,5,6,7,8,9,10]
slicing_collection(my_list)