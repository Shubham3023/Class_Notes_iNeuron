# Method Overwriting

class ineuron :

    def student(self):
        print("print details of all the students")

    def achivers(self):
        print("print the list of all achivers")

    def hall_of_fame(self):
        print("print everyone from hall of frame")

class ineuron_vision(ineuron) :

    def student(self):  # overwriting method student from parent class(Method Overwriting)
        print("these are the filtered student list")

iv = ineuron_vision()

iv.student()