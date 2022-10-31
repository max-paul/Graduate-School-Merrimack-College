class Person:
    def __init__(self, name, familyName, age):
        """
        Constructor for Peron
        :param name:
        :param familyName:
        :param age:
        """
        self.self = self
        self.name = name
        self.familyName = familyName
        self.age = age

    def getName(self):
        """
        Get Name of Person
        :return: Name
        """
        return self.name

    def getFullName(self):
        """
        Get Full name of person
        :return: FullName
        """
        return self.name + " " + self.familyName

    def getFamilyName(self):
        """
        Get Family name
        :return: Family Name
        """
        return self.familyName

    def getAge(self):
        """
        returns the age value of the person
        :return: Age
        """
        return self.age
