class Calculator:
    def __init__(self, n):
        self.n = n
    @staticmethod
    def greet():
        print("Namaste!")
    def square(self):
        print("The square of the no.", n, "is:", n**2)
        print(f"The square of the no. {n} is: {n**2}")
    def cube(self):
        print("The cube of the no.", n, "is:", n**3)
        print(f"The cube of the no. {n} is: {n**3}")
    def squareroot(self):
        print("The squareroot of the no.", n, "is:", n**(1/2))
        print(f"The squareroot of the no. {n} is: {n**(1/2)}")
n = int(input("Enter the desired number: "))


a = Calculator(n)
a.greet()
a.square()
a.cube()
a.squareroot()

Calculator(n).greet()
Calculator(n).square()
Calculator(n).cube()
Calculator(n).squareroot()