def convert_words_to_numbers(name):
    result = {(letter, name.count(letter)) for letter in name}
    return result



name = input("enter a word: ")
print(convert_words_to_numbers (name))