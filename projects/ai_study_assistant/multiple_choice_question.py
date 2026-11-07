from study_question import StudyQuestion

class MultipleChoiceQuestion(StudyQuestion):
    def __init__(self, subject: str, 
                 question: str, 
                 answer: str, 
                 max_mark: int, 
                 choices:list[str]
                 ) -> None:
        super().__init__(subject,question,answer,max_mark)

        if answer not in choices:
            raise ValueError("Correct answer is not in the available choices")
        
        self.choices = choices

    def display_question(self) -> str:
        output: str = super().display_question()
        letter_code: int = 65

        for each_choice in self.choices:
            output += f"\n{chr(letter_code)}. {each_choice}"
            letter_code += 1
        
        return output

    def evaluate_answer(self, student_answer: str) -> int:
        awarded_marks: int = super().evaluate_answer(student_answer)

        if awarded_marks == self.max_mark:
            return awarded_marks
        else:
            if (chr(65 + self.choices.index(self.answer)).lower() == student_answer.strip().lower()):
                return self.max_mark
            else:
                return 0



        








