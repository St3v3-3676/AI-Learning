class Student:
    def __init__(self, name: str, age: int, grade: int):
        self.name = name
        self.update_age(age)
        self.grade = grade


    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade {self.grade}")
        print(f"Is an adult? {self.is_adult()}")
    
    def is_adult(self) -> bool:
        return self.age >= 18

    def update_age(self, new_age: int) -> None:
        if new_age < 0 or new_age > 120:
            raise ValueError("Invalid student age")
        self._age = new_age

student1 = Student("Alex",14,8)
student1.display_info()
print()

student2 = Student("Sam",15,8)
student2.display_info()
print()

student3 = Student("Jordan",16,10)
student3.display_info()
print()

student4 = Student("Steve",18,10)
student4.display_info()
print()

student5 = Student("Chris",5,9)
student5.display_info()
print()

student6 = Student("Steve",15,10)
student6.display_info()
print()
student6.update_age(-10)
student6.display_info()
