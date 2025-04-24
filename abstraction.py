class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
    
    def start(self):
        self.clutch=True
        self.acc=True
        print("car started")


class Account:
    def __init__(self,account_no):
        self.__balance=0
        self.acc_no=account_no
    
    def debit(self,debit_amount):
        if self.__balance>=debit_amount:
            self.__balance-=debit_amount
            print(f"Balance after debit: {self.__balance}")
        else:
            print(f"Balance not sufficient, Balance : {self.__balance}")
    
    def credit(self,credit_amt):
        self.__balance+=credit_amt
        print(f"Balace after creditr : {self.__balance}")
    
    def check_balance(self):
        print(f"Balance is : {self.__balance}")

car1=Car()
car1.start() #Abstraction (As we hide working from main function)

acc1=Account("abc")
acc1.debit(100)
acc1.credit(500)
# acc1.__balance=1000
acc1.check_balance()
# print(acc1.__balance)