class StudentProfile:
    def __init__(self, name:str, year_group: int, subject: str):
        self.name = name
        self.year_group = year_group
        self.subject = subject

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        name = name.strip()

        if not name:
            raise ValueError("Name cannot be empty.")

        self._name = name

    @property
    def year_group(self) -> int:
        return self._year_group
    
    @year_group.setter 
    def year_group(self, year_group: int) -> None:
        if year_group < 7 or year_group > 11:
            raise ValueError("Year group must be between 7 and 11.")

        self._year_group = year_group

    @property
    def subject(self) -> str:
        return self._subject

    @subject.setter
    def subject(self, subject: str) -> None:
        subject = subject.strip()

        if not subject:
            raise ValueError("Subject cannot be empty.")

        self._subject = subject

    def display_profile(self) -> str:
        return f"Student Name: {self.name}\nYear Group: {self.year_group}\nSubject: {self.subject}"