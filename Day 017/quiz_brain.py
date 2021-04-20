from typing import List
from question_model import Question
import random


class Quiz:
    def __init__(self, questions: List[Question]) -> None:
        self.score = 0
        self.question_bank = questions
        random.shuffle(self.question_bank)
        self.cur_q = 0

    def can_ask(self) -> bool:
        return self.cur_q != len(self.question_bank)

    def ask(self) -> None:
        print("\n\n")
        self.cur_q += 1
        chose_question = self.question_bank[self.cur_q - 1]
        ans = input(
            f"Q.{self.cur_q}: {chose_question.question} (True/False)?: "
        ).upper()
        self.check_answer(ans)

    def check_answer(self, ans: str) -> None:
        chose_question = self.question_bank[self.cur_q - 1]
        if ans[0] == chose_question.answer[0]:
            self.score += 1
            print("You got it right!")
            print(f"The correct answer was: {chose_question.answer}.")
            print(f"Your current score is: {self.score}/{self.cur_q}")
        else:
            print("That's wrong.")
            print(f"The correct answer was: {chose_question.answer}.")
            print(f"Your current score is: {self.score}/{self.cur_q}")
