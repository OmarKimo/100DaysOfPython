class Question:
    def __init__(self, question: str, answer: str) -> None:
        self.question = question
        self.answer = answer

    def __str__(self) -> str:
        return self.question
