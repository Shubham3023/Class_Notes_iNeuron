class Person :

    def __init__(sudh,name,surname,emailid,year_of_birth) : # its is a constructor(it passes data to class and self is a pointer
        sudh.name1 = name  # self.name is class variable and self is not a keyword(in place of self sny name can be used)
        sudh.surname = surname
        sudh.emailid = emailid
        sudh.year_of_birth = year_of_birth


    def age(sudh , current_year ) :
        return current_year - sudh.year_of_birth

anuj_var = Person("anuj", "bhandari", "anuj@gmail.com", 1994)  #anuj_var is a object(class variable)
sudh = Person("sudhanshu ", "kumar", "s.kumar@gmail.com",1901)
gargi = Person("gargi","xyz","gargi@gmail.com",1991)

print(sudh.age(2022))
print(anuj_var.age(2022))
