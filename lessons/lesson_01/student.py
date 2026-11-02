from person import Person

class Student(Person):
    def __init__(self, student_id: str, name: str, age: int, grade: int):
        super().__init__(name, age)
        self._student_id = student_id
        self.grade = grade

    @property
    def student_id(self):
        return self._student_id

    @property
    def student_id(self):
        return self._student_id

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return NotImplemented

        return self.student_id == other.student_id

    def __hash__(self) -> int:
        return hash(self.student_id)


    def display_info(self):
        super().display_info()
        print(f"Grade {self.grade}")
        print(f"Student ID: {self.student_id}")

