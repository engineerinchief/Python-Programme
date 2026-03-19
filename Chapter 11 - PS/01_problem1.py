class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j ")
        

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")


i = int(input("Enter the vector: "))
j = int(input("Enter the vector: "))
k = int(input("Enter the vector: "))


a = TwoDVector(i, j)

a.show()
b = ThreeDVector(i, j, k)
b.show()