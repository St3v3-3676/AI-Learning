import pytest
from models.quiz import Quiz
from models.quiz_result import QuizResult
from models.study_question import StudyQuestion
from models.multiple_choice_question import MultipleChoiceQuestion

@pytest.fixture
def quiz() -> Quiz:
    study_question: StudyQuestion = StudyQuestion("Computer Science","How many bits are there in a byte?","8",2)
    multiple_choice_question: MultipleChoiceQuestion = MultipleChoiceQuestion(subject = "Computer Science",
                                question = "What does CPU stand for?",
                                answer = "Central Processing Unit",
                                max_mark = 3,
                                choices = [
                                    "Central Processing Unit",
                                    "Computer Processing Utility",
                                    "Central Program Unit",
                                    "Computer Power Unit"
                                ]
                                )

    quiz: Quiz = Quiz("Computer Science Revision",[study_question,multiple_choice_question])
    return quiz

def test_quiz_constructor_invalid_number_of_questions() -> None:
    with pytest.raises(ValueError):
        quiz: Quiz = Quiz("Computer Science Revision",[])

def test_correct_quiz_title(quiz: Quiz) -> None:
    assert(quiz.title) == "Computer Science Revision"

def test_for_2_quiz_questions(quiz:Quiz) -> None:
    assert(len(quiz.questions)) == 2

def test_valid_quiz_total_marks(quiz: Quiz) -> None:
    assert quiz.calculate_quiz_total_marks() == 5

def test_quiz_marking_for_valid_data() -> None:
    quiz: Quiz = Quiz("Geography Quiz",[
             StudyQuestion("Geography","What is the capital of France?","Paris",2),
             StudyQuestion("Geography","What is the capital of Germany?","Berlin",3)])

    quiz_result = quiz.mark_quiz(["Paris","Madrid"])

    assert isinstance(quiz_result, QuizResult)
    assert quiz_result.total_marks_available == 5
    assert quiz_result.marks_awarded == 2
    assert quiz_result.percentage == pytest.approx(40.0)

def test_quiz_marking_of_short_answer_and_multiple_choice_questions_full_marks(quiz: Quiz) -> None:
    quiz_result = quiz.mark_quiz(["8","A"])

    assert quiz_result.total_marks_available == 5
    assert quiz_result.marks_awarded == 5
    assert quiz_result.percentage == pytest.approx(100.0)

def test_quiz_marking_of_short_answer_and_multiple_choice_questions_partial_marks(quiz: Quiz) -> None:
    quiz_result = quiz.mark_quiz(["8","B"])

    assert quiz_result.total_marks_available == 5
    assert quiz_result.marks_awarded == 2
    assert quiz_result.percentage == pytest.approx(40.0)

@pytest.mark.parametrize("student_answers,expected_marks,expected_percentage",[
    [["8","A"],5,100.0],
    [["8","B"],2,40.0],
    [[],0,0.0]])
def test_quiz_marking_with_various_answers(quiz: Quiz, student_answers: list[str], expected_marks: int, expected_percentage: float) -> None:
    quiz_result = quiz.mark_quiz(student_answers)

    assert quiz_result.marks_awarded == expected_marks
    assert quiz_result.percentage == pytest.approx(expected_percentage)
    assert quiz_result.total_marks_available == 5

def test_quiz_marking_with_more_answers_than_questions(quiz: Quiz):
    with pytest.raises(ValueError,match="There are too many answers submitted. There should only be a maximum of 2 answers"):
        quiz.mark_quiz(["8","A","B"])

        