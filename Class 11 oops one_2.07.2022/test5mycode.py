
import logging
logging.basicConfig(filename="test5mycode.log", level=logging.DEBUG, format='%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info("this is my logging initialisation")

class Person :
     logging.info("this is my class Person")

     #constructor function with exceptionhandelling
     try:
         def __init__(self, name, dob, gender):
             self.name = name
             self.dob = dob
             self.gender = gender

     except Exception as e:
         logging.exception(e)


     try:

         def age_cal(self,current_year):
             logging.info("your age is %s", current_year - self.dob )
             return "your age is:  {}".format(current_year - self.dob)

     except Exception as e:
         logging.exception(e)

anuj_obj = Person("Anuj verma", 2004, "M")

try:
    print("Your name is: ",anuj_obj.name)
    print("Your Date of Birth is: ",anuj_obj.dob)
    print("Your Gender is: ",anuj_obj.gender)
    print(anuj_obj.age_cal(2022))
except Exception as e:
    logging.exception(e)

import logging



class Person1 :

    def get_username_emailid(self) :
        try:
            emailid = input("please enter your email id: ")
            username = ""
            for i in emailid:
                if i != "@":
                    username += i
                else:
                    break
            logging.info("your username is: {}".format(username))
            return "your username is: {}".format(username)

        except Exception as e:
            logging.exception(e)


shub_obj = Person1()

try:
    print(shub_obj.get_username_emailid())
except Exception as e:
    logging.exception(e)
