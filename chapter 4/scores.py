student_score1 = 50
student_score2 = 50
student_score3 = 50
student_score4 = 50
student_score5 = 50

scores = [50, 34, 45, 50, 25]
cart= ['banana', 33, 'juice', 2.5,["fish","palm oil"], True]
print(cart[4][1])
print("we have",len(scores), "scores")
scores2 = scores[0:3:2]

print()
print(scores[2])
for score in scores:
	print(score)
for index in range(len(scores)):
	print(index)

for index, value in enumerate(cart):
	print(index, value)

print(list(enumerate(cart))[4])

for value in enumerate(cart):
	print(value)

#scores.append(99)
#scores.pop(1)
cart[4].insert(0,6)
#scores.extend([34, 67, 87, 65])
print(scores) 
new_list = cart + scores
#print(scores[-2])
#print(scores[0:3])
print(scores[::2])