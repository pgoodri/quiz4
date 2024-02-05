from typing import Protocol

class Shape(Protocol):
    def area(self) -> float:
        ...

    def perimeter(self) -> float:
        ...

class Rectangle:
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width

    def perimeter(self) -> float:
        return 2 * (self.length + self.width)
    
class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        import math
        return 2 * math.pi * self.radius
    
def main():
    # Creating instances of Rectangle and Circle
    rectangle = Rectangle(4, 5)
    circle = Circle(3)

    # Calculating area and perimeter
    print("Rectangle:")
    print("Area:", rectangle.area())
    print("Perimeter:", rectangle.perimeter())

    print("\nCircle:")
    print("Area:", circle.area())
    print("Perimeter:", circle.perimeter())  

if __name__ == "__main__":
    main()