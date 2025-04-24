# @property
class Student:
    def __init__(self,math,science,history):
        self.math=math
        self.science=science
        self.history=history
        self.percentage=(self.math+self.history+self.science)/3
        # self.perc=self.percentage
    @property
    def perc(self):
        return (self.math+self.history+self.science)/3

stud1=Student(10,20,30)
print(stud1.percentage)
stud1.history=90
print(stud1.percentage) #this doesn't get calculated automatically
print(stud1.perc) # this gets caclculated automatically
        