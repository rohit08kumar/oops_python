# define a circle class to create a circle with radius r using the constructor.
# Define an Area() methid of the calss which calculates the area od the circle
# define a Perimeter() method od the calss which allows you to calculate the perimeter of the circle.


class Circle:
    def __init__(self,radius):
        self.radius=radius
    def calc_area(self):
        self.area=3.14*(self.radius**2)
    def calc_perimeter(self):
        self.perimeter=3.14*2*self.radius

circle1=Circle(5)
circle1.calc_area()
circle1.calc_perimeter()
print(circle1.radius)
print("Area: ", circle1.area)
print("perimeter: ", circle1.perimeter)


''' Define a Employee class with attributes role, department and salary. Thsi class also has showDetails() method.'''

class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
    def showDetails(self):
        print(f"Role : {self.role}, department: {self.dept}, salary:- {self.salary}")

class Engineer(Employee):
    def __init__(self,name,age):
        super().__init__("Engineer", "IT", 20000)
        self.name=name
        self.age=age
    # def showDetails(self):
    #     super().showDetails()
    #     print(f"name :- {self.name}, age :- {self.age}")

emp1=Employee("Scientist","Development",10000)
emp1.showDetails()

eng1=Engineer("Kapil",32)
eng1.showDetails()



''' Create a class called Order which stores item and its price.
use Dunder function __gt__() to convey that:
    order1>order2 if price of order1>price of order 2
'''

class Orders:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    
    def __gt__(cls1,cls2):
        return cls1.price>cls2.price

order1=Orders("itemA",10000)
order2=Orders("itemB",2000)
print(order1>order2)
