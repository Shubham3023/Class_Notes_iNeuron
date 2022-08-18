

import logging
logging.basicConfig(filename="test2mycode.log", level= logging.INFO, format='%(levelname)s %(asctime)s %(message)s')

logging.info("this is test run for logging")


import test1mycode

print(test1mycode)
obj2_test1 = test1mycode.Person1("Anuj", "Verma",2004)

print(obj2_test1.dob)
print(obj2_test1._name)
print(obj2_test1._Person1__surname)

print("your avg age is: ",obj2_test1.avg_age(2024))

class Person :


    dob = 1995
    _name = "shubham"
    __surname = "singh"

    def _age_cal(self,current_year):
        try:
            return current_year - self.dob

        except Exception as e:
            logging.exception(e)

    def __age1_cal(self, current_year):
        try:
            return current_year - self.dob

        except Exception as e:
            logging.exception(e)


obj1_Person = Person()

try:
    print(obj1_Person.dob)
    print(obj1_Person._name)
    print(obj1_Person._Person__surname)

    print(obj1_Person._age_cal(2022))
    print(obj1_Person._Person__age1_cal(2022))
except Exception as e:
    logging.exception(e)


class Employee(Person):

    _name = "shub"
    __surname = "sharma"
    dob = 1990
    def get_username_mail(self):
        try:
            emailid = input("enter your email id: ")
            username = ""
            for i in emailid:
                if i != "@":
                    username += i
                else:
                    break
            logging.info("User name is: %s", username)
            return "your Username is: {}".format(username)
        except Exception as e:
            logging.exception(e)

obj1_employ = Employee()

try:

    print(obj1_employ.dob)
    print(obj1_employ._name)
    print(obj1_employ._Employee__surname)

    print(obj1_employ._age_cal(2022))
    print(obj1_employ._Person__age1_cal(2022))
    print(obj1_employ.get_username_mail())
except Exception as e:
    logging.exception(e)

