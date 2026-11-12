import pytest
from controllers.quiz_controller import QuizController
from models.quiz import Quiz
from models.quiz_result import QuizResult
from models.study_question import StudyQuestion
from unittest import mock

@pytest.fixture
def quiz_controller() -> QuizController:
     return QuizController(Quiz("Computer Science",[            
                StudyQuestion(
                    "Computer Science",
                    "How many bits in a byte?",
                    "8",
                    2),
                StudyQuestion(
                    "Computer Science",
                    "How many bytes in a Kibibyte?",
                    "1024",
                    2)
                    ]    
                )
            )

def test_quiz_controller_submits_correct_answer() -> None:
    study_question: StudyQuestion = StudyQuestion("Computer Science","How many bits in a byte?","8",2)
    quiz: Quiz = Quiz("Computer Science",[study_question])
    quiz_controller: QuizController = QuizController(quiz)
    quiz_result: QuizResult = quiz_controller.submit_answers(["8"])
    
    assert isinstance(quiz_controller, QuizController)
    assert isinstance(quiz_result, QuizResult)
    assert quiz_result.total_marks_available == 2
    assert quiz_result.marks_awarded == 2
    assert quiz_result.percentage == pytest.approx(100.0)


def test_quiz_controller_calls_mark_quiz_once() -> None:
    mock_quiz = mock.Mock(spec=Quiz)
    
    expected_result = QuizResult(2, 2)
    mock_quiz.mark_quiz.return_value = expected_result  

    quiz_controller: QuizController = QuizController(mock_quiz)

    actual_result = quiz_controller.submit_answers(["8"])
    
    mock_quiz.mark_quiz.assert_called_once_with(["8"])
    assert actual_result is expected_result

def test_quiz_controller_propagates_value_error() -> None:
    #This ARRANGES a fake/mock quiz and configures it to raise a ValueError
    mock_quiz = mock.Mock(spec=Quiz)
    mock_quiz.mark_quiz.side_effect = ValueError("Too many answers")

    #This ACTS by creating a quiz_controller instance and configures it with the fake/ moc quiz
    quiz_controller: QuizController = QuizController(mock_quiz)

    #This ASSERTS that a ValueError is propagated from the quiz class to 
    #verify that the exception reaches the caller (quiz_controller)
    with pytest.raises(ValueError):
       quiz_controller.submit_answers(["8"])

def test_reset_quiz(quiz_controller: QuizController) -> None:
    quiz_controller.current_index = 1

    quiz_controller.add_student_answer("8")
    quiz_controller.add_student_answer("1024")
    assert len(quiz_controller.student_answers) == 2
    quiz_controller.reset_quiz()

    
    assert quiz_controller.current_index == 0
    assert quiz_controller.student_answers == []

@pytest.mark.parametrize("starting_index, expected_index",
                         [(0,1),
                          (1,1)
                          ]
                        )
def test_next_question(quiz_controller: QuizController, starting_index: int, expected_index: int) -> None:
        quiz_controller.current_index = starting_index
        quiz_controller.next_question()

        assert quiz_controller.current_index == expected_index
