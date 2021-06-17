from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

questions = [
    Question(question=item["question"], answer=item["correct_answer"])
    for item in question_data
]

gui = QuizInterface(quiz_brain=QuizBrain(questions))
