import re

text = "A U.S PHONE NUMBER 123-456-7890"
wrong_text = "my account number is 0092455368"

pattern2 = re.findall(r'\d\d\d-\d\d\d-\d\d\d\d', text)
pattern3 = re.findall(r'\b/d+/b', wrong_text)

print(pattern2)
print(pattern3)
#
# text2 = "my email is abc@gmail.com"
# #pattern4 = re.findall(r'[a-zA-Z]+@+gmail\.com', text2)
# #print(pattern4)
# text3 = "his email is yemi@yemi@gmail.com"
# #pattern5 = re.findall(r'[a-zA-Z]+@+gmail\.com', text3)
# a_pattern = re.compile(r'[a-zA-Z]+@+gmail\.com')
# print(a_pattern.findall(text2))
# print(a_pattern.findall(text3))
#pattern5 = re.findall(r'\b[a-zA-Z0-9._%+-]+@gmail\.com\b', text3)

# print(pattern5)

text1 = "aboy@gmail.com"
text2 = "yemi@yemi@gmail.com"

the_pattern = re.findall(r'(^[\w@][a-z]+@gmail|yahoomail\.[a-z]+)', text2)

print(the_pattern)

text6 = "Alice and Bob are Good Friends"
pattern6 = re.findall(r'\b[A-Z][a-z]+\b', text6)
print(pattern6)

text7 = "Hello! How are you doing?"
pattern7 = re.findall(r'[A-Za-z]\w+', text7)
print(pattern7)
