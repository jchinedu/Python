#trying the multiple choice quiz with objects and classes
from question import Question 
question_prompts = [
	"what color are apples?\n (A) Red/Green\n (B) Purple\n (C) Orange\n\n",
	"what color are banana?\n (A) Teal\n (B) Magenta\n (C) Yellow\n\n",
	"what color are strawberries?\n (A) Yellow\n (B) Red\n (C) Blue\n\n",
]

questions = [
	Question(question_prompts[0], "A"),
	Question(question_prompts[1], "C"),
	Question(question_prompts[2], "B")

]
def run_test(questions):
	score = 0
	for question in questions:
		answer = input(question.prompt)
		if answer ==question.answer:
			score += 1
		else:
			print('you got the wrong answer, but keep going')
	print("you got " + str(score) + "/" + str(len(questions)) + "correct")
run_test(questions)
