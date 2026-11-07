import pytest
from study_question import StudyQuestion

@pytest.fixture
def study_question() -> StudyQuestion:
    return StudyQuestion("Computer Science","What does the term CPU stand for?","Central Processing Unit",3)

@pytest.mark.parametrize("max_mark", [-5,0])
def test_invalid_mark_constructor(max_mark: int) -> None:
    with pytest.raises(ValueError):
        StudyQuestion("Computer Science","What does the term CPU stand for?","Central Processing Unit",max_mark)

@pytest.mark.parametrize("max_mark", [2.5,"five",True,False,None])
def test_invalid_max_mark_type(max_mark: object, study_question: StudyQuestion) -> None:
    with pytest.raises(TypeError):
        study_question.max_mark = max_mark

@pytest.mark.parametrize("max_mark", [-5,0])
def test_invalid_max_mark_value(max_mark: int, study_question: StudyQuestion) -> None:
    with pytest.raises(ValueError):
        study_question.max_mark = max_mark

@pytest.mark.parametrize("max_mark",[1,2,5])
def test_valid_max_mark(max_mark: int, study_question: StudyQuestion) -> None:
    study_question.max_mark = max_mark

    assert study_question.max_mark == max_mark

def test_study_question_constructor_attributes(study_question: StudyQuestion) -> None:
    assert study_question.subject == "Computer Science"
    assert study_question.question == "What does the term CPU stand for?"
    assert study_question.answer == "Central Processing Unit"
    assert study_question.max_mark == 3

def test_question_display_formating(study_question: StudyQuestion) -> None:
    assert study_question.display_question() == "Question: What does the term CPU stand for?\nMarks: 3\n"

@pytest.mark.parametrize("max_mark", [2.5,"five",True,False,None])
def test_invalid_property_type_value_preserves_state(max_mark: object, study_question: StudyQuestion) -> None:
    
    with pytest.raises(TypeError):
        study_question.max_mark = max_mark

    assert study_question.max_mark == 3

@pytest.mark.parametrize("max_mark", [-5,0])
def test_invalid_property_value_preserves_state(max_mark: object, study_question: StudyQuestion) -> None:
    
    with pytest.raises(ValueError):
        study_question.max_mark = max_mark

    assert study_question.max_mark == 3

@pytest.mark.parametrize("student_answer", [
                            "Central Processing Unit",
                            "central processing unit",
                            "  CENTRAL PROCESSING UNIT  "])
def test_correct_evaluate_answer_for_correct_answer(student_answer: str, study_question: StudyQuestion) -> None:
    assert study_question.evaluate_answer(student_answer) == study_question.max_mark
    
@pytest.mark.parametrize("student_answer", [
                            "Computer Processing Unit",
                            "CPU",
                            "",
                            "1234"])
def test_incorrect_evaluate_answer_for_correct_answer(student_answer: str, study_question: StudyQuestion) -> None:
    assert study_question.evaluate_answer(student_answer) == 0