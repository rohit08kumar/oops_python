# class Student:
#     name="Rohit"

# s1=Student()
# print(s1)
# print(s1.name)


class Student:
    def __init__(self,name,marks):
        # print("Constructor Called")
        self.name=name
        self.marks=marks
    def welcome(self):
        print("Welcome Student")
    
    def get_marks(self):
        return self.marks
    
    def get_average(self):
        return print(f"Average marks of {self.name} is: ",sum(self.marks)/3)
    
    @staticmethod #decorator
    def hello():
        print("hello")

s1=Student("Rohit",[20,30,40])
print(s1.name,s1.marks)

# s2=Student("Kapil",30)
# print(s2.name,s2.marks)
s1.welcome()
s1.get_marks()
s1.get_average()
s1.name="Kapil"
s1.get_average()
s1.hello()