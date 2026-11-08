from ai_study_assistant.study_question import StudyQuestion


class Quiz:
    def __init__(self, title: str, questions: list[StudyQuestion]) -> None:
        self.title = title
        self.questions = questions