def main():
    scores = [[78, 45, 70, 59], [33, 80, 56, 47], [54, 20, 67]]
    for index, score in enumerate(scores):
        for inner_index, inner_value in enumerate(score):
            print(f"inner value: ", inner_value, end = '\t')
            print(f"inner value: ", inner_value)
            print(f"inner list: ", score, end = '\t')
            print(f"inner list index: ", index)




#collect the number and return it in words
def convert_numbers_to_words(numbers):
    number_to_words = {
        '1':"one",
        '2': "two",
        '3': "three",
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '10': 'ten',
    }
    return number_to_words.get(numbers, "invalid number")
if __name__ == '__main__':
    numbers = (input("enter a number: "))
    number_to_words = convert_numbers_to_words(numbers)
    print(f"the number is {numbers} with {number_to_words} words")
