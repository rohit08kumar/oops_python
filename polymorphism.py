# Operator Overloading

# > (__gt__) operator overloading

class Orders:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    
    def __gt__(cls1,cls2):
        return cls1.price>cls2.price

order1=Orders("itemA",10000)
order2=Orders("itemB",2000)
print(order1>order2)



## Function Overloading
'''
Below tyoe of function overloading supported in C++, not in Python
class Abc:
    def func(self):
        print("function without parameter called")
    def func(self,abc):
        print("function with 1 parameter called")
    def func(self,abc,xyz):
        print("function with 2 parameter called")

a=Abc()
a.func()
a.func(1)
a.func(1,2)
'''
# workaround of above
class Abc:
    def func(self,*args):
        if len(args)==0:
            print("function without parameter called")
        if len(args)==1:
            print("function with 1 parameter called")
        if len(args)==2:
            print("function with 2 parameter called")

a=Abc()
a.func()
a.func(1)
a.func(1,2)



# Method Overrriding
# Only possible in case of inheritance

class Animal():
    def speak(self):
        print("Animal Speaks")

class Dog(Animal):
    def speak(self):
        print("Bark")

class Cat(Dog,Animal):
    def speak(self):
        super().speak()
        print("Meow")

a=Animal()
d=Dog()
c=Cat()
print(Cat.mro())
a.speak()
d.speak()
c.speak()


# Duck Typing

class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

def animal_sound(animal):
    animal.speak()

animal_sound(Dog())
animal_sound(Cat())
