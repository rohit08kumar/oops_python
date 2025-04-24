class A:
    def __init__(self):
        print("Welcome to Class A")
        # super().__init__()
    varA="nameA"
    def greet(self):
        print("Greet A")
class B(A):
    def __init__(self):
        print("Welcome to Class B")
        super().__init__()
    varB="nameB"
    def greet(self):
        print("Greet B")
        super().greet()
class C(A):
    def __init__(self):
        print("Welcome to Class C")
        super().__init__()
    varC="nameC"
    def greet(self):
        print("Greet C")
        super().greet()
class D(B,C):
    def __init__(self):
        print("Welcome to Class D")
        super().__init__()
    def __init_subclass__(cls):
        return super().__init_subclass__()
    varD="nameD"
    def greet(self):
        print("Greet D")
        super().greet()
d1=D()
print(d1.varA)
print(d1.varB)
print(d1.varC)
print(D.mro())
d1.greet()
