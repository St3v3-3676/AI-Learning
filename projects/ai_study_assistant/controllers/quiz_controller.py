from models.quiz import Quiz
from models.quiz_result import QuizResult

class QuizController:
    def __init__(self, quiz: Quiz) -> None:
        self.quiz = quiz

    def submit_answers(self, student_answers: list[str]) -> QuizResult:
        return self.quiz.mark_quiz(student_answers)


    