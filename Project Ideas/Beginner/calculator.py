class Calculator:
    def __init__(self):
        print("This is a calculator application utilizing OOPS coded in python. This is a beginner project.")

        self.takeInput()
        if self.operation == '*':
            self.mul()
        elif self.operation == '/':
            self.div()
        elif self.operation == '+':
            self.add()
        elif self.operation == '-':
            self.sub()
        else:
            print("Only supported operations are +, -, /, *")
            exit(1)
        print(self.answer)
    
    def takeInput(self):
        self.num1 = float (input("Enter the first number : "))
        print()
        self.operation = input("Enter the operation (*,-,+,/): ")
        print()
        self.num2=float  (input ("Enter the second number : "))
        print()
    
    def add(self):
        self.answer = self.num1 + self.num2
    def sub(self):
        self.answer = self.num1 - self.num2
    def mul(self):
        self.answer = self.num1 * self.num2
    def div(self):
        if self.num2 ==0:
            print('Error: Div by zero is not allowd :DDD')
            exit(1)
        else:
            self.answer = self.num1 / self.num2

calcObj = Calculator()