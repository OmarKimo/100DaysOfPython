import random


class QuizBrain:
    def __init__(self, questions):
        self.score = 0
        self.question_bank = questions
        random.shuffle(self.question_bank)
        self.cur_q = 0

    def can_ask(self) -> bool:
        return self.cur_q != len(self.question_bank)

    def ask(self):
        #print("\n\n")
        self.cur_q += 1
        chose_question = self.question_bank[self.cur_q - 1]
        return chose_question.question

    def check_answer(self, ans: str):
        chose_question = self.question_bank[self.cur_q - 1]
        if ans[0] == chose_question.answer[0]:
            self.score += 1
            return True
        else:
            return False
