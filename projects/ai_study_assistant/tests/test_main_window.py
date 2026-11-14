import pytest
from PySide6.QtCore import Qt
from controllers.quiz_controller import QuizController
from models.quiz import Quiz
from models.study_question import StudyQuestion

from gui.main_window import MainWindow

@pytest.fixture
def quiz_controller() -> QuizController:
    quiz: Quiz = Quiz("Computer Science", 
                          [StudyQuestion("Computer Science",
                                         "How many bits are there in a byte?",
                                         "8",
                                         2),
                            StudyQuestion("Computer Science",
                                          "How many bytes are there in a KibiByte?",
                                          "1024",2)])

    return QuizController(quiz)

@pytest.fixture
def main_window(quiz_controller: QuizController,qtbot) -> MainWindow:
    main_window: MainWindow = MainWindow(quiz_controller)
    qtbot.addWidget(main_window)
    main_window.show()

    return main_window

def test_start_quiz_displays_question_number(quiz_controller: QuizController, main_window: MainWindow, qtbot) -> None:
    #ACT
    qtbot.mouseClick(main_window.start_button, Qt.MouseButton.LeftButton)

    #ASSERT
    assert main_window.question_number_label.text() == "Question 1 of 2"
    assert main_window.question_label.text() == f"Question: How many bits are there in a byte?\nMarks: 2\n"
    assert main_window.start_button.isHidden()
    assert main_window.answer_button.isVisible()
    assert main_window.answer_button.isEnabled()
    assert main_window.next_question_button.isVisible()
    assert not(main_window.next_question_button.isEnabled())

def test_submit_answer(quiz_controller: QuizController, main_window: MainWindow, qtbot) -> None:
    #ARRANGE
    qtbot.mouseClick(main_window.start_button, Qt.MouseButton.LeftButton)

    #ACT
    qtbot.keyClicks(main_window.answer_input, "8")
    qtbot.mouseClick(main_window.answer_button, Qt.MouseButton.LeftButton)

    #ASSERT
    assert quiz_controller.student_answers == ["8"]
    assert not(main_window.answer_button.isEnabled())
    assert main_window.next_question_button.isEnabled()

def test_next_question_button(quiz_controller: QuizController, main_window: MainWindow, qtbot) -> None:
    #ARRANGE
    qtbot.mouseClick(main_window.start_button, Qt.MouseButton.LeftButton)

    #ACT
    qtbot.keyClicks(main_window.answer_input, "8")
    qtbot.mouseClick(main_window.answer_button, Qt.MouseButton.LeftButton)
    qtbot.mouseClick(main_window.next_question_button, Qt.MouseButton.LeftButton)

    #ASSERT
    assert main_window.question_number_label.text() == "Question 2 of 2"
    assert main_window.question_label.text() == "Question: How many bytes are there in a KibiByte?\nMarks: 2\n"
    assert main_window.answer_input.text() == ""
    assert main_window.answer_button.isEnabled()
    assert not(main_window.next_question_button.isEnabled())
    assert quiz_controller.student_answers == ["8"]

def test_complete_quiz(quiz_controller: QuizController, main_window: MainWindow, qtbot) -> None:
    #ARRANGE
    qtbot.mouseClick(main_window.start_button, Qt.MouseButton.LeftButton)
    #ACT
    qtbot.keyClicks(main_window.answer_input, "8")
    qtbot.mouseClick(main_window.answer_button, Qt.MouseButton.LeftButton)
    qtbot.mouseClick(main_window.next_question_button, Qt.MouseButton.LeftButton)
    qtbot.keyClicks(main_window.answer_input, "1024")
    qtbot.mouseClick(main_window.answer_button, Qt.MouseButton.LeftButton)
    #ASSERT
    assert quiz_controller.student_answers == ["8","1024"]
    assert main_window.result_label.text() == "Your score: 100.0%"
    assert main_window.reset_quiz_button.isVisible()
    assert main_window.reset_quiz_button.isEnabled()
    assert not(main_window.answer_button.isVisible())
    assert not(main_window.next_question_button.isVisible())

# def test_reset_quiz(main_window: MainWindow, qtbot) -> None:
#     #ARRANGE
#     qtbot.mouseClick(main_window.start_button, Qt.MouseButton.LeftButton)
#     qtbot.keyClicks(main_window.answer_input, "8")
#     qtbot.mouseClick(main_window.answer_button, Qt.MouseButton.LeftButton)
#     qtbot.mouseClick(main_window.next_question_button, Qt.MouseButton.LeftButton)
#     qtbot.keyClicks(main_window.answer_input, "1024")
#     qtbot.mouseClick(main_window.answer_button, Qt.MouseButton.LeftButton)
#     #ACT
#     qtbot.mouseClick(main_window.reset_quiz_button, Qt.MouseButton.LeftButton)
#     #ASSERT
    

