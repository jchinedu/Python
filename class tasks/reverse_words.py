def reverse_words(text):
    result = ""
    word = ""

    for char in text:
        if char != ' ':
            word += char
        else:
            result += word[::-1]  
            result += ' '         
            word = ''             

    result += word[::-1]  
    return result