def convert_words_to_numbers(name):
    result = {}
    for word in name:
        result[word] = result.get(word, 0) + 1
    return result

name = input("enter a word: ")
print(convert_words_to_numbers(name))