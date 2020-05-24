"""
Object-oriented programming allows for variables to be used at the class level or the instance level.
Variables are essentially symbols that stand in for a value you’re using in a program.

At the class level, variables are referred to as class variables,
whereas variables at the instance level are called instance variables.

Use class variable when you know that this variable value will be constant and with respect to instance it won't be changed.
"""
class person:
    hike = 1.5

    def __init__(self, name):
        self.name = name
    def salary(self, salary):
        print(self.name +" earns salary of rupees: " + str(salary * person.hike))


p1 = person("Sanjit")
p1.salary(10)
person.hike = 1.6
p1.name = "Anmol"
p1.salary(10)
