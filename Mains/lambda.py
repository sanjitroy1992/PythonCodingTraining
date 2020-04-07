# x = lambda a,b:a*b
# print(x(2,3))

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello {}, hope you are doing well!".format(str(self.name).title()))
# p1 = person("sanjit", 10)
# p2 = person('anmon', 15)
# print(p1.name)
# print(p2.name)
# p2.myfunc()
# print(p1.age)
class student(person):
    def __init__(self,cname,cage):
        print(cname,cage)

x = student('sanjit', 21)
x.myfunc()