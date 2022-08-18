
import logging
logging.basicConfig(filename="test1mycode.log", level= logging.INFO, format='%(levelname)s %(asctime)s %(message)s')

logging.info("this is logging test")

from utils.utilsmycode import Person2

logging.info("i have imported person2 from utils utilsmycode")

obj_new = Person2("geeta", "shankar", 2390)

print(obj_new.age_calculator(2022))
print(obj_new.dob)
print(obj_new.name)
print(obj_new.surname)

logging.info("i have used age_calculator")



class Person1 :

    # initialising constructor function
    try:

        def __init__(self, name, surname, dob):
            self._name = name
            self.__surname = surname
            self.dob = dob

        def avg_age(self,currentyear):
            return currentyear - self.dob

    except Exception as e:
        logging.exception(e)

obj_person = Person1("shubham", "verma", 1994)

try:
    print(obj_person.dob)
    print(obj_person._name)
    print(obj_person._Person1__surname)

except Exception as e:
    logging.exception(e)



