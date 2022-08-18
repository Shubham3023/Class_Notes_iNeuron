#how to use test1.py file code in test2.py file ---> by using modules
import test1   #importing a module

print(test1)
obj3 = test1.person1("sudha", "kum", 19949809)
print(obj3.yob1)
print(obj3._name1)
print(obj3._person1__surname1)



# code of test2 file is below

class person:  # parent class

    # variable creation without __init__
    #it is done to eliminate passing of variable value while creating class object
    _name = "sudh"
    __surname = "kumar"
    yob = 1990

    def _age(self,current_year):  # protected function
        return current_year - self.yob

    def __age1(self, current_year): # private function
        return current_year - self.yob

obj = person()
print(obj)
print(obj._age(2022))
print(obj._person__age1(2022))


# it is inheritance example i.e. child class employee inherit parent class person

class employee(person):  # child class
    _name = "sudhanshu"
    __surname = "singh"
    yob = 1991

obj1 = employee()

print(obj1)
print(obj1.yob)
print(obj1._name) #no hint available for protected variable
print(obj1._person__surname)
print(obj1._employee__surname) #no hint available for private variable

print(obj1._age(2022))
print(obj1._person__age1(2028))






