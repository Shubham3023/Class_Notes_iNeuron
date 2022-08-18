# polymorphism i.e 1 function with multiple behaviour

class ineuron :

    def students(self):
        print("print students details")


class class_type :

    def students(self):
        print("print the class type of students")

def ineuron_external(a):
    a.students()


i = ineuron()
j = class_type()

ineuron_external(i)

ineuron_external(j)

"""
for example
def test(a,b):
    return a+b
print(test(3,4))
print(test("sudh ", "Kumar"))
"""


"""
class
object
constructor
inheritance
private
public
protected
abstraction
encaptulations
polymorpsim
package
modules
method overrridding

For all the concepts that we have discussed in our class point by point you have to write
atleast 10 examples

you have to make sure that use ineuron studnets , class , class type , number of courses
, affiliates , blog, internship , jobs as a reference example
"""