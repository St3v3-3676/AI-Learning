import pytest
from student_profile import StudentProfile

@pytest.fixture
def student() -> StudentProfile:
    return StudentProfile("Alice", 10, "Mathematics")

def test_student_profile(student: StudentProfile) -> None:
    assert student.name == "Alice"
    assert student.year_group == 10
    assert student.subject == "Mathematics"

@pytest.mark.parametrize("year", [-5,4,6,12,16])
def test_invalid_year_group(year: int, student: StudentProfile) -> None:
    with pytest.raises(ValueError):
        student.year_group = year
        
    assert student.year_group == 10

@pytest.mark.parametrize("year",[7,8,9,10,11])
def test_valid_year_group(year: int, student: StudentProfile) -> None:
    student.year_group = year

    assert student.year_group == year

def test_invalid_name(student: StudentProfile) -> None:
    with pytest.raises(ValueError):
        student.name = "  "

    assert student.name == "Alice"

def test_invalid_subject(student: StudentProfile) -> None:
    with pytest.raises(ValueError):
        student.subject = "  "

    assert student.subject == "Mathematics"

@pytest.mark.parametrize("year", [-5,4,6,12,16])
def test_invalid_year_group_constructor(year: int) -> None:
    with pytest.raises(ValueError):
        StudentProfile("Alice",year,"Mathematics")

def test_update_subject(student: StudentProfile) -> None:
    student.subject = "Computer Science"
    assert student.subject == "Computer Science"

def test_whitespace_removal(student: StudentProfile) -> None:
    student.subject = "  Computer Science  "
    assert student.subject == "Computer Science"
