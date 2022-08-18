# data abstraction

class ineuron:
     __student = "data science"

     def student_ineuron(self):
         return "students are studying {} in ineuron".format(self.__student)

i = ineuron()

# this will print as variable i part of function in class
print(i.student_ineuron())

# actual variable __student cannot be accessed

#i.__student
