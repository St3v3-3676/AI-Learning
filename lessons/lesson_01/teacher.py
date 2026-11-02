from person import Person

class Teacher(Person):
    def __init__(self, name: str, age: int, subject: str):
        super().__init__(name, age)
        self.subject = subject

    def display_info(self):
        super().display_info()
        print(f"Subject: {self.subject}")
