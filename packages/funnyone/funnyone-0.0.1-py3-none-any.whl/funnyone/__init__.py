class Calc:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
        print("Constructer Start")
    
    def add(self):
        return self.number1 + self.number2
    
    def mul(self):
        return self.number1 * self.number2
    
    def div(self):
        return self.number1 / self.number2
    
    def sub(self):
        return self.number1 - self.number2