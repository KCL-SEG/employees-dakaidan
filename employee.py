"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from enum import Enum

class EmployeeContract(Enum):
    HOURLY = 1
    SALARIED = 2

class EmployeeCommission(Enum):
    NONE = 1
    CONTRACT = 2
    BONUS = 3

class Contract:
    def __init__(self, contractType=EmployeeContract.SALARIED, rate=0, hours=0):
        self.contractType = contractType
        self.rate = rate
        self.hours = hours

    def get_pay(self):
        if self.contractType == EmployeeContract.HOURLY:
            return self.hours * self.rate
        elif self.contractType == EmployeeContract.SALARIED:
            return self.rate
        else:
            return 0

    def __str__(self):
        if self.contractType == EmployeeContract.HOURLY:
            return f"contract of {self.hours} hours at {self.rate}/hour"
        elif self.contractType == EmployeeContract.SALARIED:
            return f"monthly salary of {self.rate}"
        else:
            return "unknown contract"


class Commission:
    def __init__(self, commission_type=EmployeeCommission.NONE, amount=0, contracts=0):
        self.commission_type = commission_type
        self.amount = amount
        self.contracts = contracts#

    def get_commission(self):
        if self.commission_type == EmployeeCommission.CONTRACT:
            return self.contracts * self.amount
        elif self.commission_type == EmployeeCommission.BONUS:
            return self.amount
        else:
            return 0

    def __str__(self):
        if self.commission_type == EmployeeCommission.CONTRACT:
            return f" and receives a commission for {self.contracts} contract(s) at {self.amount}/contract"
        elif self.commission_type == EmployeeCommission.BONUS:
            return f" and receives a bonus commission of {self.amount}"
        else:
            return ""

class Employee:
    def __init__(self, name, contract, commission):
        self.name = name
        self.contract = contract
        self.commission = commission

    def get_pay(self):
        return self.contract.get_pay() + self.commission.get_commission()

    def __str__(self):
        return f'{self.name} works on a {self.contract}{self.commission}.  Their total pay is {self.get_pay()}.'


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', contract=Contract(rate=4000), commission=Commission())

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', contract=Contract(contractType=EmployeeContract.HOURLY, rate=25, hours=100), commission=Commission())

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', contract=Contract(rate=3000), commission=Commission(commission_type=EmployeeCommission.CONTRACT, amount=200, contracts=4))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', contract=Contract(contractType=EmployeeContract.HOURLY, rate=25, hours=150), commission=Commission(commission_type=EmployeeCommission.CONTRACT, amount=220, contracts=3))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', contract=Contract(rate=2000), commission=Commission(commission_type=EmployeeCommission.BONUS, amount=1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', contract=Contract(contractType=EmployeeContract.HOURLY, rate=30, hours=120), commission=Commission(commission_type=EmployeeCommission.BONUS, amount=600))
