from data import question_data
from question_model import Question
from quiz_brain import Quiz

questions = [Question(item["text"], item["answer"]) for item in question_data]
quiz = Quiz(questions)

while quiz.can_ask():
    quiz.ask()

print("\n\nYou've finished the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.cur_q}")