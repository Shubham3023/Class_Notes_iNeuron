# overriding method

class college:

    def students(self):
        return "total no of students is: ", 100

    def stu_maths(self, maths):
        return "students studying maths : ", 100 - maths

class ineuron(college):

    def students(self):
        return "students taking ineuron course after college", 40

i = ineuron()

# methods from college
print("from college: ", i.students())  # this students method is overridden in ineuron class
print("from college: ", i.stu_maths(69))

# method from ineuron

print("from ineuron", i.students())
