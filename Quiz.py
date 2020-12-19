class Question :

    def __init__(self, prompt, answer) :
        self.prompt = prompt
        self.answer = answer

# type your questions along some options        
question_prompts = [
    "\nHow many premier league matches did United win under SAF ?\n(a) 571/810\n(b) 528/810\n(c) 562/810\n\n",
    "\nHow many goals did Cristiano Ronaldo score for United ?\n(a) 118\n(b) 134\n(c) 84\n\n",
    "\nHow many Champions League Finals did United play ?\n(a) 6\n(b) 5\n(c) 7\n\n"
]

# enter the index of the question with the correct answer
questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "b")
]

# function to run the quiz and to give the final score
def run_test(questions):
    score = 0
    for question in questions :
        answer = input(question.prompt)
        if answer == question.answer :
            score += 1
    print ("You got " + str(score) + "/" + str(len(questions)) + " correct." )    

run_test(questions)        
