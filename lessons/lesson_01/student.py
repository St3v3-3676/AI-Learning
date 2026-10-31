class Student:
    def __init__(self, name: str, age: int, grade: int):
        self.name = name
        self.age = age
        self.grade = grade


    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade {self.grade}")
        print(f"Is an adult? {self.is_adult()}")
    
    def is_adult(self) -> bool:
        return self.age >= 18

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if value < 0 or value > 120:
            raise ValueError("Invalid student age")
        self._age = value

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
student6.age = 10
student6.display_info()

print(student1.age)
student1.age = 10
print(student1.age)
