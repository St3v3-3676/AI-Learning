class StudentProfile:
    def __init__(self, name:str, year_group: int, subject: str)
        self.name = name
        self.year_group = year_group
        self.subject = subject

    @property
    def year_group(self) -> int:
        return self._year_group
    
    @year_group.setter
    def year_group(self, year_group: int):
        if year_group < 7 or year_group > 11:
            raise ValueError("Year group must be between 7 and 11.")

        self._year_group = year_group

