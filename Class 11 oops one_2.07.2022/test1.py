
class Person :

    def __init__(self,name,surname,emailid,year_of_birth) : # its is a constructor(it passes data to class and self is a pointer
        self.name = name  # self.name is class variable and self is not a keyword(in place of self sny name can be used)
        self.surname = surname
        self.emailid = emailid
        self.year_of_birth = year_of_birth


anuj_var = Person("anuj", "bhandari", "anuj@gmail.com", 1994)  #anuj_var is a object(class variable)
sudh = Person("sudhanshu", "kumar", "s.kumar@gmail.com",3123)
gargi = Person("gargi","xyz","gargi@gmail.com",871234)
print(anuj_var.name)
print(anuj_var.surname)
print(anuj_var.emailid)
print(anuj_var.year_of_birth)

print(sudh.name)
print(gargi.name)
print(gargi.emailid)

print(type(sudh))


