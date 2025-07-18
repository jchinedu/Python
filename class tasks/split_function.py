def function_split(word,string_word):
        if len(word) % 2 != 0:
            return word + string_word
        else:
            middle = len(word) // 2
            return word[:middle] + string_word + word[middle:]
print(function_split("helloo","ce"))
