# del keywords and Private attributes
class Students:
    __college="abc"
    def __init__(self,name):
        self.name=name
    
    def __hello(self,name):
        print(f"Hello {name}")
    
    def welcome(self):
        self.__hello(self.name)
    def print_name(self):
        print(self.name)
        print(self.age)
    def print_college(self):
        print(self.__college)

s1=Students("Rohit")
print(s1.name)
del s1.name
print(s1.name)
s1.name="Kapil"
print(s1.name)
s1.age=33
print(s1.age)
s1.print_name()
s1.__hello() # Will give error as __hello is provate class
s1.welcome()
print(s1.__college()) #Will give error 
s1.print_college()
s1.__college="xyz"
print(s1.__college)  ## Watch here....here it is printing the local object properties created in above line not the abject properties in class
s1.print_college()
