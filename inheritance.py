class Car:
    __color="black"
    def __init__(self):
        print("entered Parent Class")

    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stopped..")
    
    def __print_color_parent(self):
        print(f"parent class private")#: {self.__color}")
    @staticmethod
    def details():
        print("This is Fortuner Class")

    def details():
        print("This is Car Class")


class Toyotacar(Car):
    __make="Toyota"
    def __init__(self,type):
        # super().__init__()
        print("Enetered Toyota Class")
        self.__type=type
    def __print_color(self):
        # print(f"Print from BAse: {self.__color}") # it will give an error
        # self.__print_color_parent() # it will gove an error
        self._Car__print_color_parent()
    
    def _print_color(self):
        # print(f"Print from BAse: {self.__color}") # it will give an error
        # self.__print_color_parent() # it will gove an error
        self._Car__print_color_parent() # this is the correct way to access private function of parent class
    def print_type(self):
        print(self.__type)
    @staticmethod
    def details():
        print("This is Fortuner Class")

    def details():
        print("This is Toyotacar Class")


class Fortuner(Toyotacar):
    model="Fortuner"
    __make="Skoda"
    def __init__(self, variant):
        super().__init__("SUV")
        self.variant=variant
    def print_color_base(self):
        self._Toyotacar__print_color() # this is the correct way to access private function of parent class
    def print_make(self):
        print("Parent Class Make:- " , self._Toyotacar__make) # this is the correct way to access private function of parent class
    def print_make_child(self):
        print("Updated make in child Class:-  ",self.__make)
    @staticmethod
    def details():
        print("This is Fortuner Class")

    
 
c1=Fortuner("SUV")
c1.start()
c1.stop()
c1._print_color()
print(c1.__type) # Will give error
c1.print_type() # Way to access private member 
print(c1.make) # will give ERROR
c1.print_make() # How parent class private member being accessed
c1.print_make_child()
c1.print_color_base()


# c2=Toyotacar("sedan")
# print(c2.make)
# print(c2.type)