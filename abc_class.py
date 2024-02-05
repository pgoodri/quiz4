from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
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