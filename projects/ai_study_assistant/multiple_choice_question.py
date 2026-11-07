from study_question import StudyQuestion

class MultipleChoiceQuestion(StudyQuestion):
    def __init__(self, subject: str, 
                 question: str, 
                 answer: str, 
                 max_mark: int, 
                 choices:list[str]
                 ) -> None:
        super().__init__(subject,question,answer,max_mark)
        self.choices = choices

    def display_question(self) -> str:
        output: str = super().display_question()
        letter_code: int = 65

        for each_choice in self.choices:
            output += f"\n{chr(letter_code)}. {each_choice}"
            letter_code += 1
        
        return output


