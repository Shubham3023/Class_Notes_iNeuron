# incapsulation concept

class ineuron:

    def __init__(self):
        self.students1 = "data science"


    def students(self):
        print(self.students1)

i = ineuron()

i.students()

i.students1 = "data anlytics"  #overriding value of variable in run time

i.students()

class ineuron1:

    def __init__(self):
        self.__students1 = "data science"


    def students(self):
        print(self.__students1)   # or print(self._ineuron1__students1)

    def student_change(self): # (part of data incapsulation)
        self.__students1 = "big data by me"

    def student_change1(self, new_value):  # this is a setter function (part of data incapsulation)
        self.__students1 = new_value
        return new_value


i1 = ineuron1()

i1.students()

print(i1._ineuron1__students1)

i1.__students1 = "big data"  # here this overriding is not working in private variable
                                # (value of private variable cannot be changed just by variable assignment)
i1.students()

i1.student_change()   # private variable value can be changed by creating a method in class(this is incapsluation)
i1.students()

print(i1.student_change1("sudhanshu"))

