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
@pytest.fixture
def multiple_choice_question_2_choices() -> MultipleChoiceQuestion:
    return MultipleChoiceQuestion(subject = "Computer Science",
                                question = "What does CPU stand for?",
                                answer = "Central Processing Unit",
                                max_mark = 1,
                                choices = [
                                    "Central Processing Unit",
                                    "Computer Processing Utility"
                                ]
                                )

@pytest.fixture
def multiple_choice_question_no_choices() -> MultipleChoiceQuestion:
    return MultipleChoiceQuestion(subject = "Computer Science",
                                question = "What does CPU stand for?",
                                answer = "Central Processing Unit",
                                max_mark = 1,
                                choices = []
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

def test_inherited_display_question(multiple_choice_question_4_choices: MultipleChoiceQuestion) -> None:
    assert multiple_choice_question_4_choices.display_question().startswith("Question: What does CPU stand for?\nMarks: 1")

@pytest.mark.parametrize("max_mark",[2.5,"five",True,False])
def test_inherited_max_mark_invalid_type_validation(max_mark: object) -> None:
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
def test_inherited_max_mark_invalid_value_validation(max_mark: object) -> None:
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

def test_multiple_choice_has_four_choices_and_lables(multiple_choice_question_4_choices: MultipleChoiceQuestion) -> None:
    output: str = "Question: What does CPU stand for?\nMarks: 1\n"
    output = output + "\nA. Central Processing Unit\nB. Computer Processing Utility\nC. Central Program Unit\nD. Computer Power Unit"
    assert multiple_choice_question_4_choices.display_question() == output

def test_multiple_choice_has_two_choices_and_lables(multiple_choice_question_2_choices: MultipleChoiceQuestion) -> None:
    output: str = "Question: What does CPU stand for?\nMarks: 1\n"
    output = output + "\nA. Central Processing Unit\nB. Computer Processing Utility"
    assert multiple_choice_question_2_choices.display_question() == output

def test_multiple_choice_has_no_choices_and_lables(multiple_choice_question_no_choices: MultipleChoiceQuestion) -> None:
    output: str = "Question: What does CPU stand for?\nMarks: 1\n"
    assert multiple_choice_question_no_choices.display_question() == output

