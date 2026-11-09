import pytest
from models.quiz_result import QuizResult

@pytest.mark.parametrize("total_marks_available",["5","five",True,False])
def test_quiz_result_constructor_invalid_total_marks_available_type(total_marks_available: object) -> None:
    with pytest.raises(TypeError):
        QuizResult(total_marks_available,1) # type: ignore[arg-type]

@pytest.mark.parametrize("total_marks_available",[-5,0])
def test_quiz_result_constructor_invalid_total_marks_available_value(total_marks_available: int) -> None:
    with pytest.raises(ValueError):
        QuizResult(total_marks_available,1)

@pytest.mark.parametrize("marks_awarded",["5","five",True,False])
def test_quiz_result_constructor_invalid_marks_awarded_type(marks_awarded: object) -> None:
    with pytest.raises(TypeError):
        QuizResult(1,marks_awarded) # type: ignore[arg-type]

@pytest.mark.parametrize("marks_awarded",[9,15])
def test_quiz_result_invalid_marks_awarded(marks_awarded: int) -> None:
    with pytest.raises(ValueError):
        QuizResult(8,marks_awarded)

@pytest.mark.parametrize("total_marks_available,marks_awarded",[(10, 1),(10, 5),(10, 10),(20, 15)])
def test_quiz_result_constructor_valid_total_marks_available_and_marks_awarded_values(total_marks_available: int, marks_awarded: int):
    quiz_result: QuizResult = QuizResult(total_marks_available,marks_awarded)

    assert quiz_result.marks_awarded == marks_awarded 
    assert quiz_result.total_marks_available == total_marks_available

@pytest.mark.parametrize("total_marks_available,marks_awarded,expected_percentage",[(20, 0, 0.0),(20, 5, 25.0),(20, 10, 50.0),(20, 15, 75.0),(20,20,100.0)])
def test_quiz_result_percentage_for_correct_percentage(total_marks_available: int, marks_awarded: int, expected_percentage: float) -> None:
    quiz_result: QuizResult = QuizResult(total_marks_available,marks_awarded)

    assert quiz_result.percentage == pytest.approx(expected_percentage)
    
   

