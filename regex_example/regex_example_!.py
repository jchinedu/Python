import re
text = "the silent boy is sick today, call this number 08161247818"

pattern = re.findall(r'\w+\s+', text)
pattern2 = re.findall(r'\d+', text)
patter3 = re.findall(r'\b/d+/b', text)
patter4 = re.findall(r'\d+', text)
patter5 = re.findall(r'\d+', text)


print(pattern, pattern2, patter3)