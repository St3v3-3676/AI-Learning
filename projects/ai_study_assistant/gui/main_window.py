import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit
from PySide6.QtCore import Qt

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from controllers.quiz_controller import QuizController
from models.quiz import Quiz
from models.study_question import StudyQuestion
from models.quiz_result import QuizResult

class MainWindow(QWidget):
    def __init__(self, quiz_controller: QuizController) -> None:
        self.quiz_controller = quiz_controller
        super().__init__()
        self.setWindowTitle("AI Study Assistant - Quiz")
        self.resize(500,350)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setSpacing(12)
        layout.setContentsMargins(20, 20, 20, 20)

        self.label_quiz_title = QLabel("Welcome to AI Study Assistant")
        self.label_quiz_select = QLabel("Select a quiz to begin")
        self.result_label = QLabel("")

        self.question_label = QLabel("")
        self.question_label.setWordWrap(True)
        self.question_label.hide()

        self.answer_input = QLineEdit()
        self.answer_input.setPlaceholderText("Enter your answer")
        self.answer_input.hide()

        self.answer_button = QPushButton("Submit Answer")
        self.answer_button.clicked.connect(self.submit_answer)
        self.answer_button.hide()

        layout.addWidget(self.label_quiz_title)
        layout.addWidget(self.label_quiz_select)
        layout.addWidget(self.question_label)
        layout.addWidget(self.answer_input)
        layout.addWidget(self.answer_button)
        layout.addWidget(self.result_label)
        

        self.start_button = QPushButton("Start Quiz")
        self.start_button.clicked.connect(self.start_quiz)
        layout.addWidget(self.start_button)

        self.setLayout(layout)

    def start_quiz(self) -> None:
        print("Starting quiz...")
        self.label_quiz_select.setText("Quiz started!")
        quiz: Quiz = self.quiz_controller.quiz
        self.question_label.setText(quiz.questions[0].display_question())
        self.question_label.show()
        self.answer_input.show()
        self.answer_button.show()
        self.start_button.hide()

    def submit_answer(self) -> None:
        student_answer = self.answer_input.text()
        quiz_result: QuizResult = self.quiz_controller.submit_answers([student_answer])
        self.result_label.setText(f"Your score: {quiz_result.percentage}%")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    quiz: Quiz = Quiz(
        "Computer Science",
            [
            StudyQuestion(
                "Computer Science",
                "How many bits in a byte?",
                "8",
                2)
            ]
    )
                                                      
    quiz_controller: QuizController = QuizController(quiz)
                                                    
    main_window = MainWindow(quiz_controller)
    main_window.show()

    sys.exit(app.exec())
