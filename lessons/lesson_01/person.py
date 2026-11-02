class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        if age < 0 or age > 120:
            raise ValueError("Invalid student age")
        self._age = age
        pass

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is an adult? {self.is_adult()}")

    def is_adult(self) -> bool:
        return self.age >= 18

