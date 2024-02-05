class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property 
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value

    @property
    def diameter(self):
        return 2 * self.radius
    
    @property
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
def main():
    # Creating a circle with radius 3
    circle = Circle(3)

    # Accessing properties
    print("Radius:", circle.radius)
    print("Diameter:", circle.diameter)
    print("Area:", circle.area)

    # Modifying radius
    circle.radius = 5
    print("\nNew Radius:", circle.radius)
    print("New Diameter:", circle.diameter)
    print("New Area:", circle.area)

    # Trying to set negative radius (should raise an error)
    try:
        circle.radius = -2
    except ValueError as e:
        print("\nError:", e)

if __name__ == "__main__":
    main()
