# Data Abstraction (hiding data from unwanted person)


class ineuron :

    __students = "data science"

    def students(self):
        print("print the class of students: ", ineuron.__students)

i = ineuron()

i.students()

# i.__students  here we are trying to hide students variable behind class ineuron.(This is data abstraction)

print(i._ineuron__students)


