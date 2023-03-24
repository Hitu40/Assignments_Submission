class Student:

    def __init__(self):
        self._name = ""
        self._rollNumber = ""

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getRollNumber(self):
        return self._rollNumber

    def setRollNumber(self, rollNumber):
        self._rollNumber = rollNumber

student = Student()
student.setName("Hitendra")
student.setRollNumber("1234")
print(student.getName()) # Output: Hitendra
print(student.getRollNumber()) # Output: 1234

'''
Output:

Hitendra
1234
'''