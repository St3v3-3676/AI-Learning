from models.quiz import Quiz
from models.quiz_result import QuizResult
from models.study_question import StudyQuestion

class QuizController:
    def __init__(self, quiz: Quiz) -> None:
        self.quiz = quiz
        self.current_index = 0
        self.student_answers: list[str] = []

    def submit_answers(self, student_answers: list[str]) -> QuizResult:
        return self.quiz.mark_quiz(student_answers)

    def get_current_question(self) -> StudyQuestion:
        return self.quiz.questions[self.current_index]

    def get_number_of_questions(self) -> int:
        return len(self.quiz.questions)

    def next_question(self) -> None:
        if self.current_index + 1 < len(self.quiz.questions):
            self.current_index += 1

    def add_student_answer(self, answer: str) -> None:
        self.student_answers.append(answer)

    def reset_quiz(self) -> None:
        self.current_index = 0
        self.student_answers = []

    