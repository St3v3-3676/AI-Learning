class StudyQuestion:
    def __init__(self, subject: str, question: str, answer: str, max_mark: int):
        self.subject = subject
        self.question = question
        self.max_mark = max_mark
        self.answer = answer

    @property
    def max_mark(self) -> int:
        return self._max_mark

    @max_mark.setter
    def max_mark(self, max_mark: int) -> None:
        if type(max_mark) is not int:
            raise TypeError("Max mark must be a whole number.")
        
        if max_mark < 1:
            raise ValueError("Max mark must be positive and at least 1.")

        self._max_mark = max_mark

    def display_question(self) -> str:
        return f"Question: {self.question}\nMarks: {self.max_mark}\n"

    def evaluate_answer(self, student_answer:str) -> int:
        if student_answer.strip().lower() == self.answer.strip().lower():
            return self.max_mark
        else:
            return 0


