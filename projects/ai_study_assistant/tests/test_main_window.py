import pytest
from unittest import mock
from PySide6.QtCore import Qt
from controllers.quiz_controller import QuizController
from models.quiz import Quiz
from models.study_question import StudyQuestion
from models.quiz_result import QuizResult

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
    assert main_window.question_label.text() == "Question: How many bits are there in a byte?\nMarks: 2\n"
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

def test_reset_quiz(quiz_controller: QuizController, main_window: MainWindow, qtbot) -> None:
    #ARRANGE
    qtbot.mouseClick(main_window.start_button, Qt.MouseButton.LeftButton)
    qtbot.keyClicks(main_window.answer_input, "8")
    qtbot.mouseClick(main_window.answer_button, Qt.MouseButton.LeftButton)
    qtbot.mouseClick(main_window.next_question_button, Qt.MouseButton.LeftButton)
    qtbot.keyClicks(main_window.answer_input, "1024")
    qtbot.mouseClick(main_window.answer_button, Qt.MouseButton.LeftButton)
    assert main_window.result_label.text() == "Your score: 100.0%"
    #ACT
    qtbot.mouseClick(main_window.reset_quiz_button, Qt.MouseButton.LeftButton)
    #ASSERT
    assert main_window.question_number_label.text() == "Question 1 of 2"
    assert main_window.question_label.text() == "Question: How many bits are there in a byte?\nMarks: 2\n"
    assert main_window.answer_input.text() == ""
    assert main_window.answer_button.isEnabled()
    assert main_window.answer_button.isVisible()
    assert main_window.next_question_button.isVisible()
    assert not(main_window.next_question_button.isEnabled())
    assert quiz_controller.student_answers == []
    assert quiz_controller.current_index == 0
    assert main_window.result_label.text() == ""

def test_complete_quiz_with_incorrect_answers(quiz_controller: QuizController, main_window: MainWindow, qtbot) -> None:
    #ARRANGE
    qtbot.mouseClick(main_window.start_button, Qt.MouseButton.LeftButton)
    #ACT
    qtbot.keyClicks(main_window.answer_input, "8")
    qtbot.mouseClick(main_window.answer_button, Qt.MouseButton.LeftButton)
    qtbot.mouseClick(main_window.next_question_button, Qt.MouseButton.LeftButton)
    qtbot.keyClicks(main_window.answer_input, "1000")
    qtbot.mouseClick(main_window.answer_button, Qt.MouseButton.LeftButton)
    assert main_window.result_label.text() == "Your score: 50.0%"
    
def test_complete_quiz_with_all_incorrect_answers(quiz_controller: QuizController, main_window: MainWindow, qtbot) -> None:
    #ARRANGE
    qtbot.mouseClick(main_window.start_button, Qt.MouseButton.LeftButton)
    #ACT
    qtbot.keyClicks(main_window.answer_input, "5")
    qtbot.mouseClick(main_window.answer_button, Qt.MouseButton.LeftButton)
    qtbot.mouseClick(main_window.next_question_button, Qt.MouseButton.LeftButton)
    qtbot.keyClicks(main_window.answer_input, "1000")
    #ASSERT
    assert not main_window.result_label.isVisible()
    print(f"Visible: {main_window.result_label.isVisible()}")
    print(f"Text: {main_window.result_label.text()!r}")
    qtbot.mouseClick(main_window.answer_button, Qt.MouseButton.LeftButton)
    assert main_window.result_label.isVisible()
    assert main_window.result_label.isEnabled()
    assert main_window.result_label.text() == "Your score: 0.0%"

def test_marking_error_displays_message_and_allows_restart(
    quiz_controller: QuizController,
    main_window: MainWindow,
    qtbot,
) -> None:
    qtbot.mouseClick(main_window.start_button, Qt.MouseButton.LeftButton)
    qtbot.keyClicks(main_window.answer_input, "8")
    qtbot.mouseClick(main_window.answer_button, Qt.MouseButton.LeftButton)
    qtbot.mouseClick(main_window.next_question_button, Qt.MouseButton.LeftButton)

    with mock.patch.object(
        quiz_controller,
        "submit_answers",
        side_effect=ValueError("Unable to mark the quiz."),
    ) as mocked_submit:
        qtbot.mouseClick(main_window.answer_button, Qt.MouseButton.LeftButton)

    assert main_window.result_label.text() == "Unable to mark the quiz."
    assert main_window.result_label.isVisible()
    assert main_window.reset_quiz_button.isVisible()
    mocked_submit.assert_called_once_with(["8", ""])

    qtbot.mouseClick(main_window.reset_quiz_button, Qt.MouseButton.LeftButton)

    assert quiz_controller.student_answers == []
    assert quiz_controller.current_index == 0
    assert main_window.result_label.text() == ""
    assert main_window.answer_button.isVisible()
    assert main_window.answer_button.isEnabled()

    qtbot.keyClicks(main_window.answer_input, "8")
    qtbot.mouseClick(main_window.answer_button, Qt.MouseButton.LeftButton)
    qtbot.mouseClick(main_window.next_question_button, Qt.MouseButton.LeftButton)
    qtbot.keyClicks(main_window.answer_input, "1024")
    qtbot.mouseClick(main_window.answer_button, Qt.MouseButton.LeftButton)

    assert main_window.result_label.text() == "Your score: 100.0%"


