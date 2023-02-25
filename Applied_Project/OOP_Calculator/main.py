from abc import ABC, abstractmethod

class Operation(ABC):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    @abstractmethod
    def perform_operation(self):
        return
    

class Addition(Operation):
#
    def perform_operation(self):
        return self.num1 + self.num2


class Subtraction(Operation):

    def perform_operation(self):
        return self.num1 - self.num2



class Multiplication(Operation):

    def perform_operation(self):
        return self.num1 * self.num2


class Division(Operation):

    def perform_operation(self):
        try:
            return self.num1 / self.num2
        
        except ZeroDivisionError:
            raise Exception("Cannot divide by Zero.")

class Exponent(Operation):
    def perform_operation(self):
        return self.num1 ** self.num2


adder = Addition(1,2).perform_operation()
subtractor = Subtraction(1,2).perform_operation()
multiplier = Multiplication(1,2).perform_operation()
divider1 = Division(1,2).perform_operation()
#divider2 = Division(1,0).perform_operation():w

#error = Operation(1,2).perform_operation()

exponent = Exponent(2,2).perform_operation()

print(adder)
print(subtractor)
print(multiplier)
print(divider1)
#print(divider2)
# print(error)
print(exponent)