from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question_loop in question_data:
    question_text = question_loop["question"]
    question_answer = question_loop["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_have_question():
    quiz.next_question()

print("you've completed the quiz")
print(f"your final score is:{quiz.score}/{quiz.question_no} ")




