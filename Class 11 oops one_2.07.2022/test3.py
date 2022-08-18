class Person :

    def __init__(sudh,name,surname,emailid,year_of_birth) : # its is a constructor(it passes data to class and self is a pointer
        sudh.name1 = name  # self.name is class variable and self is not a keyword(in place of self sny name can be used)
        sudh.surname = surname
        sudh.emailid = emailid
        sudh.year_of_birth = year_of_birth

    def __init__(sudh,name,surname) :
        sudh.name1 = name
        sudh.surname = surname


    def age(sudh , current_year ) :
        return current_year

anuj_var = Person("anuj", "bhandari")
sudh = Person("sudhanshu ", "kumar")
gargi = Person("gargi","xyz")

print(sudh.age(2022))
print(anuj_var.age(2022))
