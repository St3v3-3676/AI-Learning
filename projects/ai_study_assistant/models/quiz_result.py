class QuizResult:
    def __init__(self, total_marks_available: int, marks_awarded: int) -> None:
        if type(total_marks_available) is not int:
            raise TypeError("Total quiz marks available must be a whole number")

        if total_marks_available < 1:
            raise ValueError("Total quiz marks available cannot be less than 1")

        self.total_marks_available = total_marks_available

        if type(marks_awarded) is not int:
            raise TypeError("Quiz marks awarded must be a whole number")

        if marks_awarded > total_marks_available:
            raise ValueError("Awarded marks cannot be more that the total marks available")

        self.marks_awarded = marks_awarded

    @property
    def percentage(self) -> float:
        return self.marks_awarded / self.total_marks_available * 100
        
    
        

        

 

        