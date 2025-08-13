def reverse_words(text):
    result = ""
    word = ""

    for char in text:
        if char != ' ':
            word += char
        