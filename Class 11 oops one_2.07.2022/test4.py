class Person :
    # below are methods

    def age(self, current_year , year_of_birth):
        return current_year - year_of_birth

    def email_id_input(self, email_id):
        print("take a email id from a person and print it", email_id)


    def ask_name(self):
        name = input("tell me your name: ")
        return name

    def ask_dob(self):
        dob = input("tell me your date of birth: ")
        return dob
    # init(constructor) takes data from class variable

    #below are class object ( variable of Person class)

sudh = Person()

anuj = Person()

gargi = Person()

krish = Person()

hitesh = Person()

sudh.email_id_input("sudhanshu@ineuron.in")

print(sudh.ask_name())

print(hitesh.ask_dob())


"""
task 1 in past what ever question given wrt list tuple dict and set try to create a seperate class for each and
    every thing and
restructure your code for all the segment and submit.None

    inst 1 always use exception handeling
    inst 2 use logging as well

reformat your code and submit it to me before tommorrow class by 3 pm ist
sudhanshu@ineuron.ai
sunny.savita@ineuron.ai

"""

