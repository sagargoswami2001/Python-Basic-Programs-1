class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__phone = 9837876110


    def getphone(self):
        return self.__phone

class library (student):
    def __init__(self, name, age, fine):
        student.__init__(self, name, age)
        self.fine = fine

obj = library("Sagar Goswami", 20, 500)
print(f"\nName: {obj.name}\nAge: {obj.age}\nFine: {obj.fine}")
print(f"Phone Number: {obj.getphone()}")
