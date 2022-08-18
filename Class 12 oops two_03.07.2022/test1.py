#from test2 import person

#import utils.utils1
from utils.utils1 import person2  #utils is a package,utils1 is module, person2 is a class, and class can have methods

obj = person2("sudhanshu", "kumar", 1999)

print(obj.yob1)

# below is test1 code
class person1 :
    def __init__(self, name, surname, yob):
        self._name1 = name  #_varname  it is protected variable
        self.__surname1 = surname   #__varname  it is private variable, it won't run by default, use obj._class__varname
        self.yob1 = yob

sudh = person1("sudhanshu", "kumar", 1990)

print(sudh.yob1)  # yob 1 is a public variable
print(sudh._name1) # _name is a protected variable
print(sudh._person1__surname1)# __surname is a private variable

