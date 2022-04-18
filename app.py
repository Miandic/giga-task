

class Figure():

    def area():
        pass
    def printArea():
        print(self.area())
class Rectangle(Figure):

    def __init__(self , *args):
        if len(args) == 1 and isinstance(args[0] , int):
            self.side1 = args[0]
            self.side2 = args[0]
        elif len(args) == 2 and isinstance(args[0] , int) and isinstance(args[1] , int) :
            self.side1 = args[0]
            self.side2 = args[1]
        else:
            self.side1 = 0
            self.side2 = 0
    def area(self ):
        return self.side1 * self.side2

class Square(Rectangle):

    def __init__(self , side):
        self.side1 = side
        self.side2 = side

    def __add__(self , n):
        self.side1 += n
        self.side2 += n
r1 = Rectangle(2)
print(r1.area())
