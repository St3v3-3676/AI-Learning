import pytest
from multiple_choice_question import MultipleChoiceQuestion

@pytest.fixture
def multiple_choice_question_4_choices() -> MultipleChoiceQuestion:
    return MultipleChoiceQuestion(subject = "Computer Science",
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
@pytest.mark.parametrize("max_mark",[2.5,"five",True,False])
def test_inherited_max_mark_invalid_type_validation(max_mark: int) -> None:
    with pytest.raises(TypeError):
        MultipleChoiceQuestion(subject = "Computer Science",
                                question = "What does CPU stand for?",
                                answer = "Central Processing Unit",
                                max_mark = max_mark,
                                choices = [
                                    "Central Processing Unit",
                                    "Computer Processing Utility",
                                    "Central Program Unit",
                                    "Computer Power Unit"
                                ]
                                )

@pytest.mark.parametrize("max_mark",[-5,0])
def test_inherited_max_mark_invalid_value_validation(max_mark: int) -> None:
    with pytest.raises(ValueError):
        MultipleChoiceQuestion(subject = "Computer Science",
                                question = "What does CPU stand for?",
                                answer = "Central Processing Unit",
                                max_mark = max_mark,
                                choices = [
                                    "Central Processing Unit",
                                    "Computer Processing Utility",
                                    "Central Program Unit",
                                    "Computer Power Unit"
                                ]
                                )
        
def test_inherited_display_question(multiple_choice_question_4_choices: MultipleChoiceQuestion) -> None:
    assert multiple_choice_question_4_choices.display_question().startswith("Question: What does CPU stand for?\nMarks: 1")

@pytest.mark.parametrize("choices",[[],["Central Processing Unit"]])
def test_multiple_choice_constructor_value_error_number_of_choices(choices: list[str]) -> None:
    with pytest.raises(ValueError):
               MultipleChoiceQuestion(subject = "Computer Science",
                                        question = "What does CPU stand for?",
                                        answer = "Central Processing Unit",
                                        max_mark = 1,
                                        choices = choices
                                        )


def test_multiple_choice_constructor_answer_not_in_choices() -> None:
    with pytest.raises(ValueError):
               MultipleChoiceQuestion(subject = "Computer Science",
                                        question = "What does CPU stand for?",
                                        answer = "Central Processing Unit",
                                        max_mark = 1,
                                        choices = ["Central Process Unit",                                    
                                                    "Computer Processing Utility",
                                                    "Central Program Unit",
                                                    "Computer Power Unit"]
                                        )

def test_multiple_choice_question(multiple_choice_question_4_choices: MultipleChoiceQuestion) -> None:
    assert multiple_choice_question_4_choices.subject == "Computer Science"
    assert multiple_choice_question_4_choices.question == "What does CPU stand for?"
    assert multiple_choice_question_4_choices.answer == "Central Processing Unit"
    assert multiple_choice_question_4_choices.max_mark == 1
    assert multiple_choice_question_4_choices.choices == [
                                    "Central Processing Unit",
                                    "Computer Processing Utility",
                                    "Central Program Unit",
                                    "Computer Power Unit"
                                    ]

def test_multiple_choice_question_has_lables(multiple_choice_question_4_choices: MultipleChoiceQuestion) -> None:
    output: str = "Question: What does CPU stand for?\nMarks: 1\n"
    output = output + "\nA. Central Processing Unit\nB. Computer Processing Utility\nC. Central Program Unit\nD. Computer Power Unit"
    assert multiple_choice_question_4_choices.display_question() == output

@pytest.mark.parametrize(
    "student_answer, expected_marks",
    [
        ("A", 1),
        ("a", 1),
        ("  A  ", 1),
        ("Central Processing Unit", 1),
        ("B",0),
        ("D",0),
        ("",0)
    ]
)
def test_multiple_choice_question_evaluate_answer(
    multiple_choice_question_4_choices: MultipleChoiceQuestion,
    student_answer: str,
    expected_marks: int,
) -> None:
    assert multiple_choice_question_4_choices.evaluate_answer(student_answer) == expected_marks 

def test_multiple_choice_question_evaluate_answer_when_option_c_is_correct() -> None:
    multiple_choice_question: MultipleChoiceQuestion = MultipleChoiceQuestion(subject = "Computer Science",
                                question = "What does CPU stand for?",
                                answer = "Central Processing Unit",
                                max_mark = 1,
                                choices = [
                                    "Central Program Unit",
                                    "Computer Processing Utility",
                                    "Central Processing Unit",
                                    "Computer Power Unit"
                                ])

    assert multiple_choice_question.evaluate_answer("C") == 1
    assert multiple_choice_question.evaluate_answer("A") == 0

