import logging

logging.basicConfig(filename="utilsmycode.log", level= logging.INFO, format= '%(levelname)s %(asctime)s %(message)s')

logging.info("this is my module")

class Person2 :
     def __init__(self, name, surname, dob):
         self.name = name
         self.surname = surname
         self.dob = dob

     def age_calculator(self, CR):
         return CR - self.dob

obj_util = Person2("aarya", "singhal", 2029)

print(obj_util.name)
print(obj_util.surname)
print(obj_util.dob)
