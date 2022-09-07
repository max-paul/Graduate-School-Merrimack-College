#student class that implments name and age, assertion forces strings upon this class
from abc import ABC, abstractmethod


class Student(ABC):
    # initializing our global variables for this interface
    def __init__(self, name, age):
        self.self = self
        self.name = name
        self.age = age
        # making sure name and age are strings, if not throw assertion error.
        assert isinstance(age, str)
        assert isinstance(name, str)

    # display method to show the data within the class
    def display(self):
        print(f"The students name is: {self.name} "
              f"\nThe students age is: {self.age}\n")


# creating the engineer class
class Engineer(Student):
    # intializing the variables within the class
    def __init__(self, name, age, courses):
        # extending out Student class into engineer
        Student.__init__(self, name, age)
        self.courses = courses

    # displaying the engineer with new variables
    def displayEngineer(self):
        print(f"The students name is: {self.name} \nThe students age is: {self.age}"
              f"\nThe students courses is: {self.courses}\n")


class Doctor(Student):
    
    # intializing the variables within the class
    def __init__(self, name, age, hospital):
        Student.__init__(self, name, age)
        self.hospital = hospital

    # displaying the Doctor with new variables
    def displayDoctor(self):
        print(f"The students name is: {self.name} \nThe students age is: {self.age} "
              f"\nThe students hospital is: {self.hospital}\n")


Student("max","21").display()
Engineer("max", "12", "Comp Sci, Math, Data Mining").displayEngineer()
Doctor("max", "12", "Mass General").displayDoctor()
