# @classmethod

class Person:
    name="anonymous"
    def changename(self,name):
        self.name=name
    def changeclassname(self,name):
        Person.name=name
        print("Person Class name changed")
    def change_class_name_method_2(self,name):
        self.__class__.name=name # Above menthod and this one is same
    @classmethod #We can do the same thing like above 2 using this decorator
    def change_class_name(cls,name): # takes default input as first argument, which refer to the class (just like self)
        cls.name=name

p1=Person()
p1.changename("Rohit")
print(p1.name)
print(Person.name)
p1.changeclassname("Kapil")
print(p1.name)
print(Person.name)
p1.change_class_name_method_2("Jyoti")
print(Person.name)
p1.change_class_name("Bhutani")
print(p1.name)
print(Person.name)
p2=Person()
print(p2.name) # we can see class entiry name has been permanently changed


