from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank  = []
quiz = QuizBrain(question_bank)

for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(text = question_text, answer = question_answer)
    question_bank.append(new_question)

while quiz.still_have_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is {quiz.score} of {len(quiz.question_list)}") 