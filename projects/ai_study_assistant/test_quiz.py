import pytest
from quiz import Quiz
from study_question import StudyQuestion
from multiple_choice_question import MultipleChoiceQuestion

@pytest.fixture
def quiz() -> Quiz:
    studyQuestion: StudyQuestion = StudyQuestion("Computer Science","How many bits are there in a byte?","8",1)
    multipleChoiceQuestion: MultipleChoiceQuestion = MultipleChoiceQuestion(subject = "Computer Science",
                                question = "What does CPU stand for?",
                                answer = "Central Processing Unit",
                                max_mark = 1,
                                choices = [
                                    "Central Processing Unit",
                                    "Computer Processing Utility",
                                    "Central Program Unit",
                                    "Computer Power Unit"
                                ]
                                )

    quiz: Quiz = Quiz("Computer Science Revision",[studyQuestion,multipleChoiceQuestion])
    return quiz

def test_quiz_constructor_invalid_number_of_questions() -> None:
    with pytest.raises(ValueError):
        quiz: Quiz = Quiz("Computer Science Revision",[])

def test_correct_quiz_title(quiz: Quiz) -> None:
    assert(quiz.title) == "Computer Science Revision"

def test_for_2_quiz_questions(quiz:Quiz) -> None:
    assert(len(quiz.questions)) == 2

def test_valid_quiz_total_marks(quiz: Quiz) -> None:
    assert quiz.calculate_quiz_total_marks() == 2