"""
The setattr() function sets the value of the attribute of an object.
The syntax of the setattr() function is: setattr(object, name, value)

The getattr() method returns the value of the named attribute of an object.
Syntax: getattr(object, name[, default])

Note: getattr and setattr can be set only at the object or instance level of the class.
"""
class ABC:
    x = "This is x"

obj1 = ABC()
print(getattr(obj1, "x"))
# print(getattr(obj1, "y"))   #Notice y is not defined in ABC class y so,is not an attribute of ABC class.
setattr(obj1, "y", "This is y")
print(getattr(obj1, "y"))

obj2 = ABC()
setattr(obj2, "age", 20)
print(obj2.age)
# print(getattr(obj2, "y"))
#getattr and setattr can be set only at the object or instance level of the class.
# Hence, when y is set for obj1 it can not be called from obj2.

