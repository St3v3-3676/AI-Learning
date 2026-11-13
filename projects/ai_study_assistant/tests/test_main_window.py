import pytest
from PySide6.QtCore import Qt
from controllers.quiz_controller import QuizController
from models.quiz import Quiz
from models.study_question import StudyQuestion

from gui.main_window import MainWindow

def test_start_quiz_displays_question_number(qtbot) -> None:
    #ARRANGE
    quiz: Quiz = Quiz("Computer Science", 
                      [StudyQuestion("Computer Science",
                                     "How many bits are there in a byte?",
                                     "8",
                                     2),
                        StudyQuestion("Computer Science",
                                      "How many bytes are there in a KibiByte?",
                                      "1024",2)])
    quiz_controller: QuizController = QuizController(quiz)
    main_window: MainWindow = MainWindow(quiz_controller)
    qtbot.addWidget(main_window)
    main_window.show()
    #ACT
    qtbot.mouseClick(main_window.start_button, Qt.MouseButton.LeftButton)

    #ASSERT
    assert main_window.question_number_label.text() == "Question 1 of 2"
    assert main_window.question_label.text() == f"Question: How many bits are there in a byte?\nMarks: 2\n"